from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return """<!DOCTYPE html>
<html>
<head>
    <title>Self Introduction - Thiyagarajan V</title>
</head>
<body>
    <h1>Self Introduction</h1>
    <p>Hello, my name is <strong>Thiyagarajan V</strong>, and I completed my 
    <strong>M.Tech in Information Technology</strong> at 
    <em>B.S. Abdur Rahman Crescent Institute of Science and Technology</em>, with a CGPA of <strong>83.52%</strong>. 
    I completed my <strong>B.Tech in Information Technology</strong> from 
    <em>Adhiparasakthi Engineering College</em>, securing a CGPA of <strong>80.5%</strong>.</p>

    <p>I’m a results-driven and passionate <strong>Software Engineer</strong> with a strong foundation in 
    <em>software development, cloud computing, and DevOps automation</em>. My technical skills include:</p>
    
    <ul>
        <li>Programming: Python, Java, C++, C</li>
        <li>Cloud & DevOps: AWS, Docker, Kubernetes, Terraform, Jenkins, CI/CD</li>
        <li>Scripting: Bash, PowerShell</li>
        <li>Version Control: Git, GitHub, Bitbucket</li>
        <li>Web: HTML, CSS, JavaScript</li>
        <li>Database: SQL</li>
        <li>Operating Systems: Linux, Windows</li>
    </ul>

    <p>I have built several impactful projects, including:</p>
    <ol>
        <li>A Flask-based Result Publishing Website</li>
        <li>A Banking Chatbot using IBM Watson and AWS</li>
        <li>Phishing Detection System using Machine Learning</li>
        <li>Multi-Language Compiler with Java Swing and Spring Boot</li>
        <li>CI/CD Pipeline to Deploy Spring Boot API with Jenkins and Docker</li>
    </ol>

    <p>I am eager to apply my knowledge in a collaborative environment and contribute meaningfully to challenging software and DevOps projects.</p>
</body>
</html>"""

if __name__ == '__main__':
    app.run(debug=True,host="localhost",port=3535)