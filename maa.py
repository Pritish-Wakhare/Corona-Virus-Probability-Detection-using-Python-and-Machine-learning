from flask import Flask , render_template , request
app = Flask(__name__)
import pickle


# open a file, where you stored the pickled data
file = open('model.pkl', 'rb')

clf = pickle.load(file)



# close the file
file.close()

@app.route('/', methods =["GET", "POST"])
def hello_world():
    if request.method =="POST":
        myDict = request.form
        fever = int(myDict['fever'])
        age = int(myDict['age'])
        pain = int(myDict['pain'])
        diffbreadth = int(myDict['diffbreadth'])
        inputFeatures =[fever, age, pain, diffbreadth]
        infProb = clf.predict_proba([inputFeatures])[0][1]
        print(infProb)
        return render_template('show.html', inf=round(infProb*100))
    return render_template('index.html')



if __name__ == "__main__":
    app.run(debug=True)