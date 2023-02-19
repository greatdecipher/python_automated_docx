import datetime
from pathlib import Path
from docxtpl import DocxTemplate
import PySimpleGUI as sg

document_path = Path(__file__).parent / "fair_use_policy.docx"
doc = DocxTemplate(document_path)

today = datetime.datetime.today()
after_week = today + datetime.timedelta(days=7)

layout = [
    [sg.Text("Company name: "), sg.Input(key="company_name", do_not_clear=False)],
    [sg.Text("Requester Name: "), sg.Input(key="user", do_not_clear=False)],
    [sg.Text("Project Name: "), sg.Input(key="project" do_not_clear=False)],
    [sg.Text("Purpose: "), sg.Input(key="purpose", do_not_clear=False)],
    [sg.Text("Agreed Deposit: "), sg.Input(key="deposit", do_not_clear=False)],
    [sg.Text("Days of Usage: "), sg.Input(key="days", do_not_clear=False)],
    [sg.Button("Create Contract"), sg.Exit()],
]

window = sg.Window("SOFTWARE FAIR USE CONTRACT GENERATOR", layout, element_justification = "right")

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    if event == "Create Contract":
        if int(float(values["days"])) > 10:
            overdue = int(float(values["days"])) - 10
            values["returns"] = (int(float(values["deposit"]))-overdue*(int(float(values["deposit"])*0.02)))
        else:
            values["returns"] = 0.00

        values["company_name"]= str(values["company_name"]).title()
        values["user"]= str(values["user"]).title()
        values["project"]= str(values["project"]).title()
        values["purpose"]= str(values["purpose"]).title()
        values["today"] = today.strftime("%Y-%m-%d")
        values["after_week"] = after_week.strftime("%Y-%m-%d")

    #render the template, save new  word document  and inform user.

        doc.render(values)
        output_path = Path(__file__).parent / f"{values['user']}-contract.docx"
        doc.save(output_path)
        sg.popup("File Saved", f"File has been saved here: {output_path}")


window.close()