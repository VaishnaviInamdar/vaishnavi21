#!/usr/bin/env python
import food_recognize as vr
from flask import Flask, render_template, Response
import io
from flask import Flask, flash, redirect, render_template, request, session, abort
import json
import base64
import cv2
from datetime import datetime
app = Flask(__name__)
#vc = cv2.VideoCapture(0)
import dbConnection as dc
import time
from flask import jsonify
# Source path content all images
SOURCE_PATH = "C:/Recipe Recomendation/"

FOOD_TYPE = 'Fruit'  # 'Vegetable'
def load_food_name(food_type):
    
    names = [line.rstrip('\n').lower() for line in open('dict/' + food_type + '.dict')]
    return names
@app.route('/getInfo', methods=['GET','POST'])
def getInfo():
     
        list_foods = load_food_name(FOOD_TYPE)
        imagedata =request.form["imageData"]
        imgdata = base64.b64decode(imagedata)
        filename = 'output.jpg'  
        with open(filename, 'wb') as f:
            f.write(imgdata)
        
        veg_name=vr.vegitable_recognation()
                    
        list_foods = load_food_name(FOOD_TYPE)
        if (veg_name in list_foods):
                print(veg_name)
                available=dc.getAvailableForVeg(veg_name)
                data=""
                for row in available:
                    data= data+"#"+str(row[0])+"@"+str(row[1])+"@"+str(row[2])+"@"+str(row[3])+"@"+str(row[4])+"@"+str(row[5])
                x={"success":"success","value":str(data[1:])}
                print(json.dumps(x))
    
                return json.dumps(x)
                
                
        else:
            x={"value":str("no recipe available for this vegitable.")}
            return json.dumps(x)
            
         
@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')

@app.route('/addRecipe', methods=['GET','POST'])
def addRecipe():
    
    
    recipe_type =request.form["recipe_type"]
    recipe_title =request.form["recipe_title"]
    recipe_indgredients =request.form["recipe_ingredients"]
    recipe_procedure =request.form["recipe_procedure"]
    recipe_link =request.form["recipe_link"]
    imageData =request.form["imageData"]
    imgdata = base64.b64decode(imageData)
    filename = "static/"+recipe_title+".jpg"
    print()
    with open(filename, 'wb') as f:
            f.write(imgdata)
    
   
    dc.add_recipe(recipe_type, recipe_title, recipe_indgredients, recipe_procedure, recipe_link)
    x={"success":str("sucess"),"message":"Recipe Added Successfully."}
    return json.dumps(x)

@app.route('/deleteRecipe', methods=['GET','POST'])
def deleteRecipe():
    
    
    recipe_id =request.form["recipe_id"]
    
    dc.delete_recipe(recipe_id)
    x={"success":str("sucess"),"message":"Recipe Deleted Successfully."}
    return json.dumps(x)

@app.route('/userRegistration', methods=['GET','POST'])
def userRegistration():
    
    
    email =request.form["email"]
    password =request.form["password"]
    name =request.form["name"]
    mobile =request.form["mobile"]
    address =request.form["address"]
    
    dc.check_existing_user(email, password, name, mobile, address)
    x={"success":str("sucess"),"message":"User Registered Successfully."}
    return json.dumps(x)



@app.route('/RatingFeedback', methods=['GET','POST'])
def RatingFeedback():
    
    
    feedback =request.form["feedback"]
    rating =request.form["rating"]
    email =request.form["email"]
    date =request.form["date"]
    r_id =request.form["id"]
    
    dc.check_existing_user_feedback(email,rating,feedback,date,r_id)
    x={"success":str("sucess"),"message":"User feedback added Successfully."}
    return json.dumps(x)



@app.route('/getAllFeedback', methods=['GET','POST'])
def getAllFeedback():
    id =request.form["id"]
    ss=dc.getFeedback(id)
    ok=""
    for i in ss:
        
        one=str(i[0])+"#"+str(i[1])+"#"+str(i[2])+"#"+str(i[3])+"#"+str(i[4])
        ok=ok+"="+one
    print(ok[1:])
    x={"value":str(ok[1:]),"message":"User feedback added Successfully."}
    return json.dumps(x)







@app.route('/userLogin', methods=['GET','POST'])
def userLogin():
    
    
    email =request.form["email"]
    password =request.form["password"]
   
    name, mobile, address=dc.user_login(email,password)
    
    x={"success":str("sucess"),"name":str(name),"mobile":str(mobile),"address":str(address)}
    return json.dumps(x)




@app.route('/checkAvailable', methods=['GET','POST'])
def checkAvailableVegee():
    
    vegee_name =request.form["vegee_name"]
    
    required_procedure=dc.getRecipe(vegee_name)
    print(required_procedure)
    my_array_requirements = list()
    my_quintity = list()
    
    required=required_procedure[0].split("#")
    
    for x in required:
        
        my_quintity.append(dc.getAvailable(x))
        my_array_requirements.append(x)
        
    
    print(my_quintity)
    print(my_array_requirements)
    mystring="The requirements for "+vegee_name+ "\n are as follow: \n"
    print(len(my_quintity))
    for i in range( len(my_quintity)):
        mystring=mystring+str(my_array_requirements[i]) +" ---- "+str(my_quintity[i])+" Kg. \n"
   
    x={"value":str(mystring),"procedure":str(required_procedure[1])}
    return json.dumps(x)

        
@app.route('/getAllRecipe', methods=['GET','POST'])
def getAllRecipe():
    
    print("received")
    
    available=dc.getAllAvailable()
    print(available)
    data=""
    for row in available:
        data= data+"#"+str(row[0])+"@"+str(row[1])+"@"+str(row[2])+"@"+str(row[3])+"@"+str(row[4])+"@"+str(row[5])
    x={"value":str(data[1:])}
    print(json.dumps(x))
    
    return json.dumps(x)

@app.route('/getAllRecipeById', methods=['GET','POST'])
def getAllRecipeById():
    
    print("received")
    
    available=dc.getAllAvailable()
    print(available)
    names = list()
    my_quintity = list()
    
    
    
    for x in available:
        
        names.append(x[1])
        my_quintity.append(x[2])
        
    
    print(my_quintity)
    print(names)
    mystring="All vegetable details are as follow: \n"
    
    for i in range( len(names)):
        mystring=mystring+str(names[i]) +" ---- "+str(my_quintity[i])+" Kg. \n"

    #mystring=mystring+" Procedure is as follow: \n"+str(required_procedure[1])
       
        
    x={"value":str(mystring)}
    return json.dumps(x)
@app.route('/addPlanner', methods=['GET','POST'])
def addPlanner():
    
    
    email =request.form["email"]
    recipe_type =request.form["recipe_type"]
    recipe_title =request.form["recipe_title"]
    date_ =request.form["date"]
    dc.check_existing_plan(email, date_, recipe_type, recipe_title)
    
    x={"success":str("sucess")}
    return json.dumps(x)

@app.route('/getPlanner', methods=['GET','POST'])
def getPlanner():
    
    
    date_ =request.form["date"]
    email =request.form["email"]
    
   
    data=dc.getPlan(email, date_)
    values=""
    for i in data:
        values=values+"#"+str(i[0])+"@"+str(i[1])
        
    x={"success":str("sucess"),"value":values[1:]}
    return json.dumps(x)




if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True)
