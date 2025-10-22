from flask import Flask, render_template # type: ignore

app = Flask(__name__)

@app.route('/')
def home():
    upcoming_project = "Contact Book"
    release_date = "10/26/2025"
    return render_template('home.html', upcoming_project=upcoming_project, release_date=release_date)

@app.route('/about_me')
def about_me():
    about_info = [
        "My favorite programming language is Python.",
        "I play travel basketball.",
        "I am learning about web development with Flask and Jinja2.",
        "I have 6 siblings (including me): 3 brothers and 3 sisters.",
        "I made a campaign speech for Website Designer this year. Didn't win though.",
    ]
    return render_template('about_me.html', about_info=about_info)

@app.route('/projects')
def projects():
    projects = [
        "Portfolio Page (This project)",
        "Bank account Manager (Text-based) link: https://github.com/MRPeops01/my-first-project",
    ]
    return render_template('projects.html', projects=projects)






if __name__ == "__main__":
    app.run(debug=True)
