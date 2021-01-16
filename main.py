from flask import Flask
app = Flask(__name__)
import pickle

# open a file, where you stored the pickled data
file = open('model.pkl', 'rb')

# dump information to that file
data = pickle.load(file)

# close the file
file.close()

@app.route('/')
#dsdsad
def hello_world():
    if request.method =="POST":
        myDict = request.form
        fever = int(myDict['fever'])
        age = int(myDict['age'])
        pain = int(myDict['pain'])
        diffbreadth = int(myDict['diffbreadth'])

        #codeofinference
        inputFeatures =[fever, age, pain, diffbreadth]
        infectionProb = clf.predict_proba([inputFeatures])[0][1]

if __name__=="__main__":
    app.run(debug=True)