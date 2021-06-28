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
import tkinter as tk
 
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
 
 
# модули работы с формами и полями в формах
 
# модули валидации полей формы
 
 
# используем csrf токен, можете генерировать его сами
SECRET_KEY = 'secret'
app.config['SECRET_KEY'] = SECRET_KEY
# используем капчу и полученные секретные ключи с сайта google 
app.config['RECAPTCHA_USE_SSL'] = False
app.config['RECAPTCHA_PUBLIC_KEY'] = '6LfeLVobAAAAABvcrC05KCuTOc4gFcwJcNDwNppQ'
app.config['RECAPTCHA_PRIVATE_KEY'] = '6LfeLVobAAAAALzQMmwfO5jOVIAroZO_PN_p4zEV'
app.config['RECAPTCHA_OPTIONS'] = {'theme': 'white'}
# обязательно добавить для работы со стандартными шаблонами
 
bootstrap = Bootstrap(app)
 
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.spinbox = tk.Spinbox(self, from_=0, to=255)
        self.scale = tk.Scale(self, from_=0, to=255,
                              orient=tk.HORIZONTAL)
        self.spinbox.pack()
        self.scale.pack()
        self.btn.pack()

# создаем форму для загрузки файла
class NetForm(FlaskForm):
    # поле для введения строки, валидируется наличием данных
    # валидатор проверяет введение данных после нажатия кнопки submit
    # и указывает пользователю ввести данные если они не введены
    # или неверны
    openid = StringField('openid', validators=[DataRequired()])
    # поле загрузки файла
    # здесь валидатор укажет ввести правильные файлы
    upload = FileField('Load image', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])
    # поле формы с capture
    recaptcha = RecaptchaField()
    # кнопка submit, для пользователя отображена как send
    submit = SubmitField('send')
 
 
class IzForm(FlaskForm):
    upload = FileField('Load image', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])
    recaptcha = RecaptchaField()
    user = TextField('RGB (0-255) format : R,G,B')
    width=TextField('Width (in pixels, 2 min) format : width')
    submit = SubmitField('send')
 
 
def krest_image(file_name, choice, choice1):
    im = Image.open(file_name)
    fig = plt.figure(figsize=(6, 4))
    ax = fig.add_subplot(1,1,1)
    data = np.random.randint(0, 255, (100, 100))
    ax.imshow(im, cmap='plasma')
    b = ax.pcolormesh(data, edgecolors='black', cmap='plasma')
    fig.colorbar(b, ax=ax)
    gr_path = "./static/newgr.png"
    sns.displot(data)
    plt.savefig(gr_path)
    plt.close()
    
    stroka=''
    for e in range(0,len(choice)):
        if  (choice[e]=='1')or(choice[e]=='2')or(choice[e]=='3')or(choice[e]=='4')or\
            (choice[e]=='5')or(choice[e]=='6')or(choice[e]=='7')or(choice[e]=='8')or\
            (choice[e]=='9')or(choice[e]=='0')or(choice[e]==','):
                stroka=stroka+choice[e]
        
    zap=stroka.count(',')
    if zap==0:
        stroka=stroka+',0,0'
    if (zap==0)and(len(stroka)==0):
        stroka='0,0,0'
    if zap==1:
        stroka=stroka+',0'
    stroka1=''
      
    for e in range(0,len(choice1)):
        if  (choice1[e]=='1')or(choice1[e]=='2')or(choice1[e]=='3')or(choice1[e]=='4')or\
            (choice1[e]=='5')or(choice1[e]=='6')or(choice1[e]=='7')or(choice1[e]=='8')or\
            (choice1[e]=='9')or(choice1[e]=='0'):
                stroka1=stroka1+choice1[e]
        
    if len(stroka1)==0:
        stroka1='2'
      
    if int(stroka1)<2:
        stroka1='2'
   
    stroka=stroka+','
    stroka=stroka+stroka1
      
    W=''
    R=''    
    G=''
    B=''
    char=stroka.find(',',0,len(stroka))
    R=stroka[0:char]
    char1=stroka.find(',',char+1,len(stroka))
    G=stroka[char+1:char1]
    char2=stroka.find(',',char1+1,len(stroka))
    B=stroka[char1+1:char2]
    W=stroka[char2+1:len(stroka)]
    stroka=''
    zap=W.count(',')
    if zap>0:
        stroka=W[0:W.find(',',0,len(W))]
        W=''
        W=stroka
    if int(R)>255:
        R='255'
    if int(G)>255:
        G='255'
    if int(B)>255:
        B='255'
    if int(W)<2:
        W='2'
    x, y = im.size
    
    if (int(W)//2)>(x//2):
        W=''
        W=str(x)
    if (int(W)//2)>(y//3):
        W=''
        W=str((y//3)*2)
    
    for i in range(0, int(stroka1)):
        for j in range(0,y):
            im.putpixel((i,j),(int(R),int(G),int(B)))
        
    for i in range(x-int(stroka1), x):
        for j in range(0,y):
            im.putpixel((i,j),(int(R),int(G),int(B)))
            
    for i in range(0,x):
        for j in range(0, int(stroka1)):
            im.putpixel((i,j),(int(R),int(G),int(B)))
        
    for i in range(0,x):
        for j in range(y-int(stroka1), y):
            im.putpixel((i,j),(int(R),int(G),int(B)))
    im.save(file_name)
    ax.imshow(im)
    
 
@app.route("/lab3", methods=['GET', 'POST'])
def iz():
    form = IzForm()
    filename = None
    filename_graph=None
    if form.validate_on_submit():
        photo = form.upload.data.filename.split('.')[-1]
        filename = os.path.join('./static', f'photo.{photo}')
        filename_graph = os.path.join('./static', f'newgr.png')
        form.upload.data.save(filename)
        krest_image(filename, form.user.data, form.width.data)
    return render_template('lab3.html', form=form, image_name=filename,filename_graph=filename_graph)
 

 
 
# метод для обработки запроса от пользователя
@app.route("/apinet", methods=['GET', 'POST'])
def apinet():
    print("1")
    neurodic = {}
    # проверяем что в запросе json данные
    if request.mimetype == 'application/json':
        # получаем json данные
        print(request.__dir__())
        data = request.get_json()
        # берем содержимое по ключу, где хранится файл
        # закодированный строкой base64
        # декодируем строку в массив байт, используя кодировку utf-8
        # первые 128 байт ascii и utf-8 совпадают, потому можно
        print(data)
        filebytes = data['imagebin'].encode('utf-8')
        # декодируем массив байт base64 в исходный файл изображение
        cfile = base64.b64decode(filebytes)
        print("4")
        # чтобы считать изображение как файл из памяти используем BytesIO
        img = Image.open(BytesIO(cfile))
        decode = neuronet.getresult([img])
        neurodic = {}
        for elem in decode:
            neurodic[elem[0][1]] = str(elem[0][2])
            print(elem)
        # пример сохранения переданного файла
        # handle = open('./static/f.png','wb')
        # handle.write(cfile)
        # handle.close()
    # преобразуем словарь в json строку
    ret = json.dumps(neurodic)
    # готовим ответ пользователю
    resp = Response(response=ret,
                    status=200,
                    mimetype="application/json")
    # возвращаем ответ
    return resp
 
 
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
   


