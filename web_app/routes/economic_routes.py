# this is the "web_app/routes/economic_routes.py" file...

from flask import Blueprint, request, render_template

economic_routes = Blueprint("economic_routes", __name__)

@economic_routes.route("/economic/form")
def form():
    print("ECONOMIC FORM...")
    return render_template("economic_form.html")

@economic_routes.route('/economic/results', methods=['POST'])
def results():
    print("ECONOMIC RESULTS...")
    print(dict(request.form))
    
    # Get the user's choice from the form data
    risk_tolerance = request.form.get('risk_tolerance')
    indicator = request.form.get('indicator')
    
    return render_template("economic_results.html",
        risk_tolerance=risk_tolerance,
        indicator=indicator,
        score="Coming Soon",
        assessment="Coming Soon"
    )