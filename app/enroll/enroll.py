from flask import Blueprint 
enroll = Blueprint("enroll", __name__, url_prefix = "/enrollment")
# the blueprint function takes three argument = name of the print, 
@enroll.route("/register")
def register():
    return "<h3> This is the registration page <h3>"