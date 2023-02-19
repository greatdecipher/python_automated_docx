from pathlib import Path
import datetime
from docxtpl import DocxTemplate

document_path = Path(__file__).parent / "fair_use_policy.docx"
doc = DocxTemplate(document_path)

company_name = "Robsoftware"
user = "binrocode"
project = "Webscraper for E-comm Site"
purpose = "This is going to be used for data gathering"
today = datetime.datetime.today()
after_week = today + datetime.timedelta(days=7)
deposit = round(2234,2)
days = 15
returns = deposit - (days - 10)*(deposit*0.02)

context = {
    "company_name" : company_name.title(),
    "user" : user.title(),
    "project" : project.title(),
    "purpose" : purpose.title(),
    "today" : today.strftime("%Y-%m-%d"),
    "after_week" : after_week.strftime("%Y-%m-%d"),
    "deposit" : deposit,
    "days" : days,
    "returns" : returns,
}

doc.render(context)
doc.save(Path(__file__).parent / f"{user}-contract.docx")