from flask import Flask, render_template, redirect, url_for
from config import collection
import SaveCookies
import FetchData
from flask import redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login")
def login():
    try:
        SaveCookies.save_cookies()  # Save cookies manually
        return redirect(url_for('run_script'))  # Redirect to the run script page
    except Exception as e:
        return render_template("errors.html", data=str(e))


@app.route("/run-script")
def run_script():
    try:
        # Fetch trending topics and save to DB
        trending_data = FetchData.fetch_trending_and_save_to_db()
        Error_data = collection.find().sort("CreatedAt" , -1).limit(4)
        print(list(Error_data))
      
        if not trending_data:
            return render_template("error.html", data=list(Error_data))
        return render_template('page.html', data=trending_data)
    except Exception as e:
        return render_template("error.html", data=list(Error_data))

    
if __name__ == "__main__":
    app.run(debug=True)
