#!flask/bin/python
from flask import Flask, jsonify
from flask import make_response
from flask import abort
from flask import request
from flask import Flask, render_template
import pymysql.cursors 
import shutil
import string
import random
import json
pymysql.install_as_MySQLdb()
from pathlib import Path

app = Flask(__name__)

def dbConnection():
    #db = pymysql.connect("127.0.0.1","root","Bablu@143341","templates" )
    db_host="127.0.0.1"
    db_user="root"
    db_password="Mysql_password"
    db_name="templates"
    db = pymysql.connect(db_host,db_user,db_password,db_name )
    #db = pymysql.connect(db='templates', user='root', passwd='root', host='127.0.0.1', port=3306)
    return db

def dbCreation():
    conn = dbConnection()
    cur = conn.cursor()
    cur.execute('CREATE TABLE if not exists templates (Template_Id INT NOT NULL AUTO_INCREMENT, Template_Name VARCHAR(100) NOT NULL, render_status INT NOT NULL, PRIMARY KEY ( Template_Id ))')
    conn.close()

dbCreation()

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/templates', methods=['GET'])
def get_tasks():
    conn = dbConnection()
    cur = conn.cursor()
    cur.execute("select Template_Id,Template_Name from templates where render_status = 0")
    rows = cur.fetchall();
    conn.close()
    payload = []
    content = {}
    for result in rows:
       content = {'Template_Id': result[0], 'Template_Name': result[1]}
       payload.append(content)
       content = {}
    return jsonify(payload)

@app.route('/templates/<int:template_id>/render', methods=['POST'])
def get_task(template_id):
    conn = dbConnection()
    cur = conn.cursor()
    try:
        cur.execute("select Template_Name from templates where Template_Id = "+str(template_id))
        rows = cur.fetchone()[0];
        cur.execute("update templates set render_status = 1 where Template_Id = "+str(template_id))
        conn.commit()
        return render_template(rows+'.html', title = "Interview test" ,templateName = rows)
    except:
        return jsonify({"Msg":"Template Not Found."})

@app.route('/templates', methods=['POST'])
def create_task():
    conn = dbConnection()
    cur = conn.cursor()
    try :
        cur.execute("select Template_Id from templates ORDER BY Template_Id DESC LIMIT 1")
        last_template_id = cur.fetchone()[0] + 1
    except: 
        last_template_id = 1
    name = "Template_"+str(last_template_id)
    render = 0
    try:
        baseTemplate = Path("templates/base.html")
        if conn and baseTemplate.is_file():
            query = "INSERT INTO templates (Template_Name,render_status) VALUES ('"+name+"',"+str(render)+")"
            cur.execute(query)
            conn.commit()
            shutil.copy('templates/base.html', 'templates/'+name+".html")
            return jsonify({'msg': "A new template is created","Template Id": last_template_id,"name": name}), 201
        else:
            return jsonify({"Error":"Unable to create a Template"})
    except:
        return jsonify({"Error":"Unable to create a Template"})
if __name__ == '__main__':
    app.run(debug=True)


