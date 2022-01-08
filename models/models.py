from odoo import models,fields,api
from odoo.exceptions import UserError

class Student(models.Model):
	_name = "school.student" # model_school_student

	# _sql_constraints = [
	#     ('name_uniq', 'unique (name)', _('The name must be unique !')),
	# ]

	number = fields.Integer()
	name = fields.Char(required=True)
	description = fields.Text()
	year = fields.Date()
	cv = fields.Html(string="Resume")
	gender = fields.Selection(selection=[("male","Male"),
		("female","Female")], default="male")
	image = fields.Binary()
	is_register = fields.Boolean(readonly=True)
	degree = fields.Float()
	fees = fields.Float(help="Enter the fees of student", digits=(2,8))
	birth_date = fields.Datetime()
	class_room = fields.Many2one("school.class.room")
	subjects = fields.Many2many("school.subject")
	taxs = fields.Float(compute="_cal_taxs")
	taxs2 = fields.Float()
	student_register = fields.Selection(selection=[("draft","Not Register"),
		("part","Partily Paid"), ("register","Register")], default="draft")

	@api.depends("fees")
	def _cal_taxs(self):
		self.taxs = self.fees * 0.1

	@api.onchange("fees")
	def _onchange_fees(self):
		self.taxs2 = self.fees * 0.2

	# @api.constrains("name")
	# def _unique_name(self):
	# 	falg_found = False
	# 	students = self.env["school.student"].search([])
	# 	for student in students:
	# 		if self.name == student.name:
	# 			falg_found = True
	# 	if falg_found:
	# 		raise UserError("This name already exists !!")

	@api.model
	def create(self,vals):
		# raise UserError("You clicked the create button")
		if vals.get("description","null") != "null":
			vals["description"] = str(vals.get("description","Test "))+" Test"
		return super(Student,self).create(vals)


	def write(self,vals):


		vals["description"] = "Test 2"

		return super(Student,self).write(vals)

	def unlink(self):

		if self.gender == "male":
			raise UserError("This school is for girls only !!")

		return super(Student,self).unlink()

	def pay(self):
		self.write({"student_register":"register"})

	def pay_part(self):
		self.write({"student_register":"part"})

	def reset(self):
		self.write({"student_register":"draft"})

class Subject(models.Model):
	_name = "school.subject" # model_school_subject
	name = fields.Char()
	number = fields.Integer()

class Lesson(models.Model):
	_name = "school.lesson" # model_school_lesson
	number = fields.Integer()
	name = fields.Char()

class Room(models.Model):
	_name = "school.class.room" # model_school_class_room
	# _rec_name = "name"
	name = fields.Char()
	students = fields.One2many("school.student","class_room")

class Teacher2(models.Model):
	_name = "school.teacher"
	_inherit = "hr.employee"
	desc = fields.Char()

	category_ids =fields.Char()

class Teacher(models.Model):
	_inherit = "hr.employee"

	degree = fields.Selection([
		("1","1st Degree"),
		("2","2nd Degree"),
		("3","3rd Degree"),
		("4","4th Degree"),
		("5","5th Degree"),
	])

	