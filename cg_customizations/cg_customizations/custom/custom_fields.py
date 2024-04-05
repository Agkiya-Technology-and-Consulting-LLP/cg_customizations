
import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

def execute():
    custom_fields ={
    "Employee Advance": [
        {
            "dt": "Employee Advance",
            "fieldname": "custom_reference_advance",
            "fieldtype": "Data",
            "idx": 17,
            "insert_after": "custom_project_budget_head",
            "label": "Reference Advance",
            "translatable": 1
        },
        {
            "fieldname":"custom_advance_breakup",
            "fieldtype":"Section Break",
            "label":"Advance Breakup",
            "insert_after":"custom_approved_on"
        },
        {
            "fieldname":"custom_advances",
            "fieldtype":"Table",
            "label":"Advances",
            "insert_after":"custom_advance_breakup"
        },
        
     ],
    "Employee":[
        {
                    
            "dt": "Employee",
            "fieldname": "custom_reference_employee",
            "fieldtype": "Data",
            "idx": 21,
            "insert_after": "create_user_permission",
            "label": "Reference Employee",
            "translatable": 1,
        }
        ],
    
    "Expense Claim":[
        {
            "dt": "Expense Claim",
            "fieldname": "custom_expense_reference",
            "fieldtype": "Data",
            "idx": 11,
            "insert_after": "custom_assign_to",
            "label": "Expense Reference",
            "translatable": 1,
        }
        ],
    "Purchase Order":[
        {
            "dt": "Purchase Order",
            "fieldname": "custom_reference_advance",
            "fieldtype": "Data",
            "idx": 38,
            "insert_after": "cost_center",
            "label": "Reference Advance",
            "translatable": 1,
 
        }    
        ],     
    "Supplier":[
        {
 
        "dt": "Supplier",
        "fieldname": "custom_reference_employee",
        "fieldtype": "Data",
        "idx": 4,
        "insert_after": "country",
        "label": "Reference Employee",
        "translatable": 1
        }
        ]
    }
 
    create_custom_fields(custom_fields,update=1)