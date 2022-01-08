{
	"name": "School Management",
	"summary": "Learning Odoo",
	"description": """ Odoo Course:
	- python.
	- intro to odoo
	- create module""",
	"sequence": -100,
	"website": "www.firebits.net",
	"author": "Firebits",
	"depends":["base","hr"],
	"version": "1.0",
	"data": [
		"security/security.xml",
		"security/ir.model.access.csv",
		"views/views.xml",
		"reports/student_report.xml",

		],
	"application":True,
}