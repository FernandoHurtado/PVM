
from flask import Flask, request

from processing import do_calculation

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"], strict_slashes=False)

def adder_page():
    errors = ""
    if request.method == "POST":
        budget = None
        probability = None
        approval = None
        bcs_cg = None
        bcs_ig = None
        wcs_cg = None
        wcs_ig = None
        ethics = None

        try:
            budget = int(request.form["budget"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["budget"])

        try:
            probability = int(request.form["probability"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["probability"])

        try:
            approval = int(request.form["approval"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["approval"])

        try:
            bcs_cg = int(request.form["bcs_cg"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["bcs_cg"])

        try:
            bcs_ig = int(request.form["bcs_ig"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["bcs_ig"])
        try:
            wcs_cg = int(request.form["wcs_cg"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["wcs_cg"])

        try:
            wcs_ig = int(request.form["wcs_ig"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["wcs_ig"])

        try:
            ethics = str(request.form["ethics"])
        except:
            errors += "<p>{!r} is not valid.</p>\n".format(request.form["ethics"])

        if budget is not None and probability is not None and approval is not None and bcs_cg is not None and bcs_ig is not None and wcs_cg is not None and wcs_ig is not None:
            result, msg = do_calculation(budget, probability, approval, bcs_cg, bcs_ig, wcs_cg, wcs_ig, ethics)
            return '''
                <html>
                    <body>
                        <p>The final expected value is {result}</p>
                        <p>{msg}</p>
                        <p><a href="/PVM/">Click here to calculate again</a>
                    </body>
                </html>
            '''.format(result=result, msg=msg)

    return '''
        <html>
            <body>
                <title> Autonomous Policy Value Maximization </title>
		<h1> Autonomous Policy Value Maximization  </h1>
		
		{errors}
               
		<p>
                <form method="post" action=".">
                    <h2> Presets: </h2>
		    Select preset: <select name="preset">
		        <option value= 0> No Preset (manual entry) </option>
			<option value= 1> Medicare For All (United States) </option>
			<option value= 2> Land redistribution (South Africa) </option>
			<option value= 3> Brexit (United Kingdom) </option>
		    </select>
		    <h2> Manual Entry: </h2> 
		    <p>Budget cost (0 to 100):<input name="budget" /></p>
                    <p>Probability of success (0 to 100):<input name="probability" /></p>
                    <p>Public Approval (-100 to 100):<input name="approval" /></p>
                    <p>If the policy succeeds, common good will be (-100 to 100):<input name="bcs_cg" /></p>
                    <p>If the policy succeeds, individual good will be (-100 to 100):<input name="bcs_ig" /></p>
                    <p>If the policy fails, common good will be (-100 to 100):<input name="wcs_cg" /></p>
                    <p>If the policy fails, Individual good will be (-100 to 100):<input name="wcs_ig" /></p>
                    <h2> Evaluate: </h2>
		    Ethical System to evaluate: <select name="ethics">
                      <option value="Utilitarianism">Utilitarianism</option>
                      <option value="IdealUtilitarianism">Ideal Utilitarianism</option>
                      <option value="LiberalIndividualism">Liberal Individualism</option>
                      <option value="Egoism">Egoism</option>
                      <option value="ConsensusEthics">Consensus Ethics</option>
                      <option value="Nihilism">Nihilism</option>
                    </select>
                    <p><input type="submit" value="Do calculation" /></p>
                </form>
            </body>
        </html>
    '''.format(errors=errors)
