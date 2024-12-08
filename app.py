from flask import *
import dbm as db 
app=Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/Reg')
def Registration():
    return render_template("Registration.html")

@app.route('/Display')
def Display_records():
    data=db.selectAlllibrary()
    return render_template("Display.html",elist=data)

@app.route("/addlibrary", methods=["POST"])
def add_library():
    
    Id = request.form["Id"]
    Name = request.form["Name"]
    Bname = request.form["Bname"]
    Phone = request.form["Phone"]
    Email = request.form["Email"]
    Password = request.form["Password"]
    t=(Id, Name,Bname,Phone,Email,Password)
    e=db.addlibrary(t)
    return redirect("/Display")


@app.route("/deletelibrary")
def delete_library():
    Id=request.args.get("Id")
    f=db.deletelibrary((Id,))
    return redirect("/Display")

@app.route("/editlibrary")
def edit_library():
    Id=request.args.get("Id")
    data = db.selectlibraryById((Id,))
    return render_template("updatedisplay.html", row=data)

@app.route("/updatelibrary", methods=["POST"])
def update_library():
    Id = request.form["Id"]
    Name = request.form["Name"]
    Bname = request.form["Bname"]
    Phone = request.form["Phone"]
    Email = request.form["Email"]
    Password = request.form["Password"]
    t=(Name,Bname,Phone,Email,Password,Id)
    c=db.updatelibrary(t)
    return redirect("/Display")



if ("__name__ == __main__"):
    app.run(debug=True)
