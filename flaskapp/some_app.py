from flask import Flask
from flask import render_template
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, SubmitField, TextField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired
from flask_bootstrap import Bootstrap
from werkzeug.utils import secure_filename
import os
from flask import request
from flask import Response
import base64
from PIL import Image
from io import BytesIO
import json
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import string
 
# import lxml.etree as ET
 
app = Flask(__name__)
 
 
# декоратор для вывода страницы по умолчанию
@app.route("/")
def hello():
    return " <html><head></head> <body> Hello World! </body></html>"
 
 
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
 
 
# наша новая функция сайта
@app.route("/data_to")
def data_to():
    # создаем переменные с данными для передачи в шаблон
    some_pars = {'user': 'Ivan', 'color': 'red'}
    some_str = 'Hello my dear friends!'
    some_value = 10
    # передаем данные в шаблон и вызываем его
    return render_template('simple.html', some_str=some_str,
                           some_value=some_value, some_pars=some_pars)
 
 

 
@app.route("/apixml", methods=['GET', 'POST'])
def apixml():
    # парсим xml файл в dom
    dom = ET.parse("./static/xml/file.xml")
    # парсим шаблон в dom
    xslt = ET.parse("./static/xml/file.xslt")
    # получаем трансформер
    transform = ET.XSLT(xslt)
    # преобразуем xml с помощью трансформера xslt
    newhtml = transform(dom)
    # преобразуем из памяти dom в строку, возможно, понадобится указать кодировку
    strfile = ET.tostring(newhtml)
    return strfile
