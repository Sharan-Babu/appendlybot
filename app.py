from flask import Flask, jsonify, request
from wit import Wit

app = Flask(__name__)

@app.route('/',methods=['POST'])
def predict():
	def backend(intent):
		if intent == 'app_name':
		    return "The name of our application is Appendly"
		elif intent == 'app_func':
		    return "Our application build upon the DrChrono API and provides a lot of helpful features ranging from interactive dashboards,notification management to drug and patient management."
		elif intent == 'app_nav':
		    return "You can find a handy navigation bar to the left and search bar at the top right."
		elif intent == 'chart_location':
		    return "You can view all your charts and reports in the dashboard."
		elif intent == 'patients_list':
		    return "You can navigate to the Patient's List Page through the navigation bar which is to the left of the webpage."
		elif intent == 'edit_profile':
		    return "You can edit your profile details by either clicking on the User Profile button in the sidebar to the left or by clicking on your account avatar on the top right."
		elif intent == 'edit_website':
		    return "By clicking on the settings button hovering on the right, you can change the color of the sidebar."
		elif intent == 'notifications':
		    return "Click on Notifications button in the sidebar. In the page that opens, you can simultaneously view all your notifications and can also remove them."
		elif intent == 'send_notifications':
		    return "To send a notification, firstly select the Send Notifications option in the sidebar. Here, select a drug present in the list and fill the details in the Patients list form. After this, click on the Fire Notification button to send your notification to the concerned patient."
		elif intent == 'dashboard_features':
		    return "In the dashboard, you can vieew your monthly reports, useful metrics like drug sales and marketing report. You can also plot and visualize your custom data. Moreover, in this page, you can manage your tasks and also view your Patients list."
		elif intent == 'add_patient':
		    return "Click on the Patients List button in the sidebar. Here, click on the Add Patient button, fill the patient details and finally,click the Add to patients list button. You can now view your new patient in the list as well."
		elif intent == 'patient_use':
		    return "The Patients List page is really helpful for doctors as it allows them to quickly filter the patients with the help of powerful search features based on say,their name or ongoing medication and allows them to prioritize their patients according to their needs."
		elif intent == 'drug_use':
		    return "In the Drugs List Page you can filter the existing drugs based on various parameters and also add new drugs to the list. To add a new drug, click on the Add drug button,fill the drug details and press Add to drugs list. The existing list will be updated."
		elif intent == 'add_drug':
		    return "To add a new drug, click on the Add drug button in the Drugs List page,fill the drug details and press Add to drugs list. The existing list will be updated."  
		elif intent == 'custom_data':
		    return "The charts/reports in the dashboard can be replaced to visualize your custom data as well."
		elif intent == 'todo_list':
		    return "The todo/Today list feature on the Dashboard page lets you schedule your appointments and ensure that you do not miss them. You can filter and edit them according to your convenience."
		elif intent == 'analysis':
		    return "The Covid Prediction Feature lets you get an idea of the estimated csaes of the same over the next few days."
		elif intent == 'datasource':
		    return "The Machine Learning model trained to predict the no. of cases was trained on accurate data obtained from Kaggle."                                                              
		
	data = request.get_json(force=True)
	data.update((x, [y]) for x,y in data.items())
	prompt = str(data['prompt'])
	access_token = "62UGLHWGE5ZJPTETZKHVUFMM5GXCLQLL"
	client=Wit(access_token)
	response = client.message(prompt)
	
	try:
	    intent = response['intents'][0]['name']
	    if intent is None:
	        answer = 'Try framing the question in a different way...'
	    else:
	    	output = backend(intent)
	    	answer = output
	except:
		answer = "Try a different question"
    
	#output = {'result':message}
	return {'result':answer}

if __name__ == '__main__':
    app.run(debug=True)	
