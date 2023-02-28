import jinja2
import pdfkit

context = {}

template_loader = jinja2.FileSystemLoader("./")
template_env = jinja2.Environment(loader=template_loader)
template = template_env.get_template("pdf.html")
output_text = template.render(context)

config = pdfkit.configuration(wkhtmltopdf="/usr/local/bin/wkhtmltopdf")
pdfkit.from_string(output_text, "pdf_generated.pdf", configuration=config)