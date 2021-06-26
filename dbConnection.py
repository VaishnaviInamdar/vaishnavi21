import mysql.connector as con
import sys
import mysql
from datetime import datetime
now = datetime.now()
dt_string = now.strftime("%Y/%m/%d %H/%M/%S")
import json



def add_recipe(recipe_type, recipe_title, recipe_indgredients, recipe_procedure, recipe_video):   
        
        db = con.connect(host="localhost", user="root", password="", database="recipe_recomendation")
        cur = db.cursor()
    
        
        query="insert into tbl_recipe_details(recipe_type, recipe_title, recipe_indgredients, recipe_procedure, recipe_video) values(%s,%s,%s,%s,%s)"
        value=[recipe_type, recipe_title, recipe_indgredients, recipe_procedure, recipe_video]
        cur.execute(query,value)
        db.commit()
            
        
        
        print('Inserted')
        
def delete_recipe(id):
        
        db = con.connect(host="localhost", user="root", password="", database="recipe_recomendation")
        cur = db.cursor()
    
        
        query="delete from tbl_recipe_details where id='"+str(id)+"'"
        print(query)
               #value=[veg_name,newweight,dt_string,temperature,0]
        cur.execute(query)
        print('deleted')
                                
    
def check_existing_plan(user_id, date_, recipe_type, recipe_id):
        
        db = con.connect(host="localhost", user="root", password="", database="recipe_recomendation")
        cur = db.cursor()
    
        query="SELECT *  FROM tbl_weekly_planner where user_id  ='"+user_id+"' and date_='"+date_+"' and recipe_id='"+recipe_id+"'"
        cur.execute(query)
        names=cur.fetchall()
        if(int(len(names))>0):
            print("Recipe already exist...updating")
        
            for row in names:
               print(row[1])
               print(row[2])
               
               query="update tbl_weekly_planner set recipe_id='"+str(recipe_id)+"'"
               print(query)
               #value=[veg_name,newweight,dt_string,temperature,0]
               cur.execute(query)
               print('Updated')
                                
        else:
                query="insert into tbl_weekly_planner(user_id, date_, recipe_type, recipe_id) values(%s,%s,%s,%s)"
                value=[user_id, date_, recipe_type, recipe_id]
                cur.execute(query,value)
                db.commit()
            
        
        
                print('Inserted')


def check_existing_user(email, password, name, mobile, address):
        
        db = con.connect(host="localhost", user="root", password="", database="recipe_recomendation")
        cur = db.cursor()
    
        query="SELECT *  FROM tbl_user where email  ='"+email+"'"
        cur.execute(query)
        names=cur.fetchall()
        if(int(len(names))>0):
            print("User already exist...updating")
        
            for row in names:
               print(row[1])
               print(row[2])
               
               query="update tbl_user set email='"+str(email)+"' password='"+str(password)+"', name='"+str(name)+"', mobile='"+str(mobile)+"', address='"+str(address)+"'"
               print(query)
               #value=[veg_name,newweight,dt_string,temperature,0]
               cur.execute(query)
               print('Updated')
                                
        else:
                query="insert into tbl_user(email, password, name, mobile, address) values(%s,%s,%s,%s,%s)"
                value=[email, password, name, mobile, address]
                cur.execute(query,value)
                db.commit()
                print('Inserted')

def check_existing_user_feedback(email,rating,feedback,date,r_id):
        id, email, rating, feedback, date
        db = con.connect(host="localhost", user="root", password="", database="recipe_recomendation")
        cur = db.cursor()
    
        query="SELECT *  FROM user_feedback where r_id  ='"+r_id+"' and email='"+email+"'"
        cur.execute(query)
        names=cur.fetchall()
        if(int(len(names))>0):
            print("feedback already exist...updating")
        
            for row in names:
               print(row[1])
               print(row[2])
               
               query="update user_feedback set rating='"+str(rating)+"' ,feedback='"+str(feedback)+"' where r_id='"+r_id+"'"
               print(query)
               #value=[veg_name,newweight,dt_string,temperature,0]
               cur.execute(query)
               print('Updated')
                                
        else:
                query="insert into user_feedback(email,rating,feedback,date,r_id) values(%s,%s,%s,%s,%s)"
                value=[email,rating,feedback,date,r_id]
                cur.execute(query,value)
                db.commit()
                print('Inserted')



def getPlan(email, date_):
        
        db = con.connect(host="localhost", user="root", password="", database="recipe_recomendation")
        cur = db.cursor()
    
        query="SELECT recipe_type, recipe_id  FROM tbl_weekly_planner where user_id  ='"+email+"' and date_='"+date_+"'"
        cur.execute(query)
        names=cur.fetchall()
        if(int(len(names))>0):
           return names
        
            
def getFeedback(r_id):
        
        db = con.connect(host="localhost", user="root", password="", database="recipe_recomendation")
        cur = db.cursor()
        
        query="SELECT uf.email,name,feedback,rating,date  FROM recipe_recomendation.tbl_user tu inner join user_feedback uf on uf.email=tu.email where uf.r_id  ='"+str(r_id)+"'"
        cur.execute(query)
        names=cur.fetchall()
        if(int(len(names))>0):
           
           return names


                
def user_login(email,password):
    
    db = con.connect(host="localhost", user="root", password="", database="recipe_recomendation")
    cur = db.cursor()
    
    query="select  name, mobile, address from tbl_user where email='"+email+"' and password='"+password+"'"
    cur.execute(query)
    names=cur.fetchall()
    for row in names:
       return row[0],row[1],row[2]

    #print(names)
    db.commit()
    if(len(names)>0):
        return names
    else:
        return 'no record'


def getAllAvailable():
   
    db = con.connect(host="localhost", user="root", password="", database="recipe_recomendation")
    cur = db.cursor()
    
    query="select * from tbl_recipe_details"
    cur.execute(query)
    names=cur.fetchall()
    return names
##    for row in names:
##       return row[1],row[2]

    #print(names)
    db.commit()
    if(len(names)>0):
        return names
    else:
        return 'no record'



def getAvailableForVeg(name): 
   
    db = con.connect(host="localhost", user="root", password="", database="recipe_recomendation")
    cur = db.cursor()
    
    query="select * from tbl_recipe_details where recipe_indgredients LIKE '%"+name+"%'"
    cur.execute(query)
    names=cur.fetchall()
    print(names)
    return names

##    for row in names:
##       return row[1],row[2]

    #print(names)
    db.commit()
    if(len(names)>0):
        return names
    else:
        return 'no record'



def all_vegee_names():
    
    db = con.connect(host="localhost", user="root", password="", database="db_vegitable_recognation")
    cur = db.cursor()
    
    query="select vegee_name from tbl_recipe_details "
    cur.execute(query)
#names=cur.fetchall()
    row_headers=[x[0] for x in cur.description] #this will extract row headers
    rv = cur.fetchall()
    json_data=[]
    for result in rv:
        json_data.append(dict(zip(row_headers,result)))
    return json.dumps(json_data)



