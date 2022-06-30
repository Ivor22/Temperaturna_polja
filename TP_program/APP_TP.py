#dodati max temp i min temp na grafu kao check box ili na klik 

import sys,plotly,subprocess,os
from PyQt5.QtWidgets import QApplication, QMainWindow
import numpy as np
import plotly.graph_objects as go
import pandas as pd 
import plotly.express as px
from plotly.subplots import make_subplots
from ui39 import Ui_MainWindow
from fpdf import FPDF, HTMLMixin
from scipy.special import k0
from airium import Airium

class Example(QMainWindow,Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def pdf_1(self):
        #definirati sa checkboxovima koje podatke ukljuciti u PDF 
        a,la,talj,q,gornji_x,donji_x,gornji_y,donji_y,z1,z2,y1,y2,y3,y4,x1,x2,x3,x4,v0,v1,v2,rez_x,rez_y = self.unos()
        
        
        v=v1
        html = self.zadatak_2D_x(v,q,talj,la,a,z1,z2,y1,y2,y3,y4)
        self.zadatak_3D_z1(gornji_x,donji_x,gornji_y,donji_y,v,q,talj,la,a,z1,rez_x,rez_y)
        self.zadatak_3D_z2(gornji_x,donji_x,gornji_y,donji_y,v,q,talj,la,a,z2,rez_x,rez_y)
        self.zadatak_2D_y(v,q,talj,la,a,z1,z2,x1,x2,x3,x4)
        self.zadatak_2D_v(v,q,talj,la,a,z1,z2,v0,v1,v2)

        class MyFPDF(FPDF, HTMLMixin):
            pass

        pdf = MyFPDF()          
        pdf.add_page()

        pdf.set_font("Arial", size = 15)
        pdf.cell(200, 10, txt = f"Temperaturna polja - izvjestaj", 
                 ln = 1, align = 'C')
        pdf.cell(200, 10, txt = f"Tockasti pomicni toplinski izvor na polubeskonacnom tijelu", 
                 ln = 3, align = 'C')  
        pdf.cell(200, 10, txt = f"Uneseni podaci:", 
                 ln = 3, align = 'C')         
        pdf.cell(200, 10, txt = f"a: {str(a)}m2/s, la: {str(la)}w/mK, talj: {str(talj)}C, q: {str(q)}W",
                 ln = 4, align = 'C')
        pdf.cell(200, 10, txt = f"gornji_x: {str(gornji_x)}m, donji_x: {str(donji_x)}m, gornji_y: {str(gornji_y)}m, donji_y: {str(donji_y)}m",
                 ln = 4, align = 'C')
        pdf.cell(200, 10, txt = f"z1: {str(z1)}m, z2: {str(z2)}m, y1: {str(y1)}m",
                 ln = 4, align = 'C')
        pdf.cell(200, 10, txt = f"y1: {str(y1)}m, y2: {str(y2)}m, y3: {str(y3)}m, y4: {str(y4)}m",
                 ln = 4, align = 'C')
        pdf.cell(200, 10, txt = f"x1: {str(x1)}m, x2: {str(x2)}m, x3: {str(x3)}m, x4: {str(x4)}m",
                 ln = 4, align = 'C')
        pdf.cell(200, 10, txt = f"v0: {str(v0)}m/s, v1: {str(v1)}m/s, v2: {str(v2)}m/s",
                 ln = 4, align = 'C')
        pdf.cell(200, 10, txt = f"rez_x: {str(rez_x)}, rez_y: {str(rez_y)}",
                 ln = 4, align = 'C')
        pdf.cell(200, 10, txt = f"Graficki prikazi:",
                 ln = 4, align = 'C')
        pdf.image("zadatak_2D_x.png", x = None, y = None, w = 200, h = 0, type = '', link = '')  
        pdf.image("zadatak_2D_y.png", x = None, y = None, w = 200, h = 0, type = '', link = '')  
        pdf.image("zadatak_2D_v.png", x = None, y = None, w = 200, h = 0, type = '', link = '')  
        pdf.image("zadatak_3D_z1.png", x = None, y = None, w = 200, h = 0, type = '', link = '')  
        pdf.image("zadatak_3D_z2.png", x = None, y = None, w = 200, h = 0, type = '', link = '')  


        naziv_fajla = "tp_1.pdf"
        pdf.output(naziv_fajla) 
        print(f"PDF generiran kao {naziv_fajla}")
        print(f"{os.getcwd()}\{naziv_fajla}")
        subprocess.Popen(f"{os.getcwd()}\{naziv_fajla}",shell=True)
        
    def pdf_2(self):
        talj,d,q,roc,v,la,a,y1,y2,y3,y4,x1,x2,x3,x4 = self.Dunos()
        self.Dzadatak_2D_x(talj,d,q,roc,v,la,a,y1,y2,y3,y4)
        self.Dzadatak_2D_y(talj,d,q,roc,v,la,a,x1,x2,x3,x4)
        
        class MyFPDF(FPDF, HTMLMixin):
            pass

        pdf = MyFPDF()          
        pdf.add_page()
          
        pdf.set_font("Arial", size = 15)
        pdf.cell(200, 10, txt = f"Temperaturna polja - izvjestaj", 
                 ln = 1, align = 'C')
        pdf.cell(200, 10, txt = f"Linijski pomicni toplinski izvor na tankom limu", 
                 ln = 3, align = 'C')           
        pdf.cell(200, 10, txt = f"Uneseni podaci:", 
                 ln = 3, align = 'C')         
        pdf.cell(200, 10, txt = f"talj: {str(talj)}C, d: {str(d)}m, q: {str(q)}W, roc: {str(roc)}",
                 ln = 4, align = 'C')
        pdf.cell(200, 10, txt = f"v: {str(v)}m/s, la: {str(la)}m, a: {str(a)}W",
                 ln = 4, align = 'C')
        pdf.cell(200, 10, txt = f"y1: {str(y1)}m, y2: {str(y2)}m, y3: {str(y3)}m, y4: {str(y4)}m",
                 ln = 4, align = 'C')
        pdf.cell(200, 10, txt = f"x1: {str(x1)}m, x2: {str(x2)}m, x3: {str(x3)}m, x4: {str(x4)}m",
                 ln = 4, align = 'C')
        pdf.cell(200, 10, txt = f"Graficki prikazi:",
                 ln = 4, align = 'C')
        pdf.image("Dzadatak_2D_x.png", x = None, y = None, w = 200, h = 0, type = '', link = '')  
        pdf.image("Dzadatak_2D_y.png", x = None, y = None, w = 200, h = 0, type = '', link = '')  
        naziv_fajla = "tp_2.pdf"
        pdf.output(naziv_fajla) 
        print(f"PDF generiran kao {naziv_fajla}")
        print(f"{os.getcwd()}\{naziv_fajla}")
        subprocess.Popen(f"{os.getcwd()}\{naziv_fajla}",shell=True)
        
    def pdf_3(self):
        d,U,eta,v,I,T0,T0_1,T0_2,T0_3,T0_4,y1,y2,y3,rez_x,rez_y,Thl1,Thl2,Thl3,Thl4,rho,cp,la = self.Tunos()
        self.Tzadatak_vrijeme_E(d,U,eta,v,I,T0,T0_1,T0_2,T0_3,T0_4,y1,y2,y3,rez_x,rez_y,Thl1,Thl2,Thl3,Thl4,rho,cp,la)
        self.Tzadatak_ciklus(d,U,eta,v,I,T0,T0_1,T0_2,T0_3,T0_4,y1,y2,y3,rez_x,rez_y,Thl1,Thl2,Thl3,Thl4,rho,cp,la)
        
        class MyFPDF(FPDF, HTMLMixin):
            pass

        pdf = MyFPDF()          
        pdf.add_page()
          
        pdf.set_font("Arial", size = 15)
        pdf.cell(200, 10, txt = f"Temperaturna polja - izvjestaj", 
                 ln = 1, align = 'C')
        pdf.cell(200, 10, txt = f"Plosni toplinski izvor", 
                 ln = 3, align = 'C')           
        pdf.cell(200, 10, txt = f"Uneseni podaci:", 
                 ln = 3, align = 'C')         
        pdf.cell(200, 10, txt = f"d: {str(d)}m, U: {str(U)}V, eta: {str(eta)}, v: {str(v)}m/s, I: {str(I)}A",
                 ln = 4, align = 'C')
        pdf.cell(200, 10, txt = f"T0: {str(T0)}C, T0_1: {str(T0_1)}C, T0_2: {str(T0_2)}C, T0_3: {str(T0_3)}C, T0_4: {str(T0_4)}C",
                 ln = 4, align = 'C')
        pdf.cell(200, 10, txt = f"y1: {str(y1)}m, y2: {str(y2)}m, y3: {str(y3)}m",
                 ln = 4, align = 'C')
        pdf.cell(200, 10, txt = f"rez_x: {str(rez_x)}, rez_y: {str(rez_y)}",
                 ln = 4, align = 'C')
        pdf.cell(200, 10, txt = f"Thl1: {str(Thl1)}C, Thl2: {str(Thl2)}C, Thl3: {str(Thl3)}C, Thl4: {str(Thl4)}C",
                 ln = 4, align = 'C')
        pdf.cell(200, 10, txt = f"rho: {str(rho)}kg/m3, cp: {str(cp)}J/(kgK)), la: {str(la)}W/(mK)",
                 ln = 4, align = 'C')
        pdf.cell(200, 10, txt = f"Graficki prikazi:",
                 ln = 4, align = 'C')
        pdf.image("Tzadatak_vrijeme_E.png", x = None, y = None, w = 200, h = 0, type = '', link = '')  
        pdf.image("Tzadatak_ciklus.png", x = None, y = None, w = 200, h = 0, type = '', link = '')  

        naziv_fajla = "tp_3.pdf"
        pdf.output(naziv_fajla) 
        print(f"PDF generiran kao {naziv_fajla}")
        print(f"{os.getcwd()}\{naziv_fajla}")
        subprocess.Popen(f"{os.getcwd()}\{naziv_fajla}",shell=True)
        
    def Tzadatak_max_Temp(self,d,U,eta,v,I,T0,T0_1,T0_2,T0_3,T0_4,y1,y2,y3,rez_x,rez_y,Thl1,Thl2,Thl3,Thl4,rho,cp,la):  

        c=cp
        q=U*I*eta
        
        Tmax_y1 = ( q / ( v * d * rho * c * 2 * y1 ) ) * ( np.sqrt( 2 / ( np.pi * np.exp(1) ) ) )  + T0_2
        Tmax_y2 = ( q / ( v * d * rho * c * 2 * y2 ) ) * ( np.sqrt( 2 / ( np.pi * np.exp(1) ) ) )  + T0_2
        Tmax_y3 = ( q / ( v * d * rho * c * 2 * y3 ) ) * ( np.sqrt( 2 / ( np.pi * np.exp(1) ) ) )  + T0_2

        a = Airium()

        a('<!DOCTYPE html>')
        with a.html(lang="pl"):
            with a.head():
                a.meta(charset="utf-8")
                a.title(_t="Example: How to use Airium library")
            with a.body():
                with a.h1(id="id23345225", kclass='main_header'):
                    a(f"Temperatura predgrijavanja, T02: {round(T0_2,1)}[°C]")
                with a.h1(id="id23345225", kclass='main_header'):
                    a(f"Tmax_y1, y1={y1}[m]: {round(Tmax_y1,1)}[°C]")
                with a.h1(id="id23345225", kclass='main_header'):
                    a(f"Tmax_y2, y2={y2}[m]: {round(Tmax_y2,1)}[°C]")
                with a.h1(id="id23345225", kclass='main_header'):
                    a(f"Tmax_y3, y3={y3}[m]: {round(Tmax_y3,1)}[°C]")

        html = str(a)
        html_bytes = bytes(a)
        
        return html, q

    def Tzadatak_sirina_ZUT(self,d,U,eta,v,I,T0,T0_1,T0_2,T0_3,T0_4,y1,y2,y3,rez_x,rez_y,Thl1,Thl2,Thl3,Thl4,rho,cp,la):
        c=cp
        
        q=U*I*eta
        E=(U*I)/v
        
        E = np.linspace(1, E, int(rez_x), endpoint = True)
        
        t85_T1 = ( E**2 * eta**2 ) / ( d**2 * 4 * np.pi * la * rho * c ) * ( ( 1 / ( 500  - T0_1 )**2 ) - ( 1 / ( 800 - T0_1 )**2 ) )
        t85_T2 = ( E**2 * eta**2 ) / ( d**2 * 4 * np.pi * la * rho * c ) * ( ( 1 / ( 500  - T0_2 )**2 ) - ( 1 / ( 800 - T0_2 )**2 ) )
        t85_T3 = ( E**2 * eta**2 ) / ( d**2 * 4 * np.pi * la * rho * c ) * ( ( 1 / ( 500  - T0_3 )**2 ) - ( 1 / ( 800 - T0_3 )**2 ) )
        t85_T4 = ( E**2 * eta**2 ) / ( d**2 * 4 * np.pi * la * rho * c ) * ( ( 1 / ( 500  - T0_4 )**2 ) - ( 1 / ( 800 - T0_4 )**2 ) )       
         
        y_700 = q / ( v * d * rho * c * np.sqrt( 2 * np.pi * np.exp(1) ) ) * ( 1 / ( 700  - T0_2 ) )
        y_1500 = q / ( v * d * rho * c * np.sqrt( 2 * np.pi * np.exp(1) ) ) * ( 1 / ( 1500  - T0_2 ) )

        S_ZUT = y_700 - y_1500

        a = Airium()
        a('<!DOCTYPE html>')
        with a.html(lang="pl"):
            with a.head():
                a.meta(charset="utf-8")
                a.title(_t="Example: How to use Airium library")
            with a.body():
                with a.h1(id="id23345225", kclass='main_header'):
                    a(f"Temperatura predgrijavanja, T02: {round(T0_2,1)}[°C]")
                with a.h1(id="id23345225", kclass='main_header'):
                    a(f"Širina zone utjecaja topline: {round(S_ZUT,5)}[m]")

        html = str(a)
        html_bytes = bytes(a)
        
        return html, q


    def Tzadatak_vrijeme_E(self,d,U,eta,v,I,T0,T0_1,T0_2,T0_3,T0_4,y1,y2,y3,rez_x,rez_y,Thl1,Thl2,Thl3,Thl4,rho,cp,la):

        c=cp        
        q=U*I*eta               
        E=(U*I)/v        
        E = np.linspace(1, E, int(rez_x), endpoint = True)
        
        t85_T1 = ( E**2 * eta**2 ) / ( d**2 * 4 * np.pi * la * rho * c ) * ( ( 1 / ( 500  - T0_1 )**2 ) - ( 1 / ( 800 - T0_1 )**2 ) )
        t85_T2 = ( E**2 * eta**2 ) / ( d**2 * 4 * np.pi * la * rho * c ) * ( ( 1 / ( 500  - T0_2 )**2 ) - ( 1 / ( 800 - T0_2 )**2 ) )
        t85_T3 = ( E**2 * eta**2 ) / ( d**2 * 4 * np.pi * la * rho * c ) * ( ( 1 / ( 500  - T0_3 )**2 ) - ( 1 / ( 800 - T0_3 )**2 ) )
        t85_T4 = ( E**2 * eta**2 ) / ( d**2 * 4 * np.pi * la * rho * c ) * ( ( 1 / ( 500  - T0_4 )**2 ) - ( 1 / ( 800 - T0_4 )**2 ) )

        fig = make_subplots(rows=1, cols=1)

        fig.add_trace(go.Scatter(x=E, y=t85_T1,
                            mode='lines',
                            name=f't85,T01={T0_1}[°C]'),
                              row=1, col=1)
        fig.add_trace(go.Scatter(x=E, y=t85_T2,
                            mode='lines',
                            name=f't85,T02={T0_2}[°C]'),
                              row=1, col=1)
        fig.add_trace(go.Scatter(x=E, y=t85_T3,
                            mode='lines',
                            name=f't85,T03={T0_3}[°C]'),
                              row=1, col=1)
        fig.add_trace(go.Scatter(x=E, y=t85_T4,
                            mode='lines',
                            name=f't85,T04={T0_4}[°C]'),
                              row=1, col=1)

        fig.update_layout(height=580, width=800, title_text="t85"+"=f(E,T0) sa parametarskom vrijednošću T0")
        fig.update_layout(margin=dict(l=0, r=0, t=80, b=0))

        fig.update_xaxes(title_text="E [J/m]", row=1, col=1)
        fig.update_yaxes(title_text="t85 [s]", row=1, col=1)
        fig.write_image("Tzadatak_vrijeme_E.png")
        html2 = '<html><body>'
        html2 += plotly.offline.plot(fig, output_type='div', include_plotlyjs='cdn')
        html2 += '</body></html>'
        
        return html2, q


    def Tzadatak_vrijeme_hl(self,d,U,eta,v,I,T0,T0_1,T0_2,T0_3,T0_4,y1,y2,y3,rez_x,rez_y,Thl1,Thl2,Thl3,Thl4,rho,cp,la):

        c=cp        
        q=U*I*eta
        E=(U*I)/v
        
        t85_T1 = ( E**2 * eta**2 ) / ( d**2 * 4 * np.pi * la * rho * c ) * ( ( 1 / ( 500  - T0_1 )**2 ) - ( 1 / ( 800 - T0_1 )**2 ) )
        t85_T2 = ( E**2 * eta**2 ) / ( d**2 * 4 * np.pi * la * rho * c ) * ( ( 1 / ( 500  - T0_2 )**2 ) - ( 1 / ( 800 - T0_2 )**2 ) )
        t85_T3 = ( E**2 * eta**2 ) / ( d**2 * 4 * np.pi * la * rho * c ) * ( ( 1 / ( 500  - T0_3 )**2 ) - ( 1 / ( 800 - T0_3 )**2 ) )
        t85_T4 = ( E**2 * eta**2 ) / ( d**2 * 4 * np.pi * la * rho * c ) * ( ( 1 / ( 500  - T0_4 )**2 ) - ( 1 / ( 800 - T0_4 )**2 ) )

        a = Airium()

        a('<!DOCTYPE html>')
        with a.html(lang="pl"):
            with a.head():
                a.meta(charset="utf-8")
                a.title(_t="Example: How to use Airium library")
            with a.body():
                with a.h1(id="id23345225", kclass='main_header'):
                    a("Trenutno vrijeme hlađenja:")
                with a.h2(id="id23345225", kclass='main_header'):
                    a(f"t85_T1= {round(t85_T1,2)}[s]")
                with a.h2(id="id23345225", kclass='main_header'):
                    a(f"t85_T2= {round(t85_T2,2)}[s]")
                with a.h2(id="id23345225", kclass='main_header'):
                    a(f"t85_T3= {round(t85_T3,2)}[s]")
                with a.h2(id="id23345225", kclass='main_header'):
                    a(f"t85_T4= {round(t85_T4,2)}[s]")

        html = str(a)
        html_bytes = bytes(a)
        
        return html, q
        
    def Tzadatak_brzina_hl(self,d,U,eta,v,I,T0,T0_1,T0_2,T0_3,T0_4,y1,y2,y3,rez_x,rez_y,Thl1,Thl2,Thl3,Thl4,rho,cp,la):      

        c=cp
        q=U*I*eta
        
        dTdt_800 = - 2 * np.pi * la * rho * c * ( ( d**2 * ( Thl1 - T0 )**3 ) / ( q / v )**2 )
        dTdt_700 = - 2 * np.pi * la * rho * c * ( ( d**2 * ( Thl2 - T0 )**3 ) / ( q / v )**2 )
        dTdt_600 = - 2 * np.pi * la * rho * c * ( ( d**2 * ( Thl3 - T0 )**3 ) / ( q / v )**2 )
        dTdt_500 = - 2 * np.pi * la * rho * c * ( ( d**2 * ( Thl4 - T0 )**3 ) / ( q / v )**2 )

        a = Airium()

        a('<!DOCTYPE html>')
        with a.html(lang="pl"):
            with a.head():
                a.meta(charset="utf-8")
                a.title(_t="Example: How to use Airium library")
            with a.body():
                with a.h1(id="id23345225", kclass='main_header'):
                    a("Trenutna brzina hlađenja:")
                with a.h2(id="id23345225", kclass='main_header'):
                    a(f"dTdt_800= {round(dTdt_800,2)}[°C/s]")
                with a.h2(id="id23345225", kclass='main_header'):
                    a(f"dTdt_700= {round(dTdt_700,2)}[°C/s]")
                with a.h2(id="id23345225", kclass='main_header'):
                    a(f"dTdt_600= {round(dTdt_600,2)}[°C/s]")
                with a.h2(id="id23345225", kclass='main_header'):
                    a(f"dTdt_500= {round(dTdt_500,2)}[°C/s]")

        html = str(a)
        html_bytes = bytes(a)

        return html, q
        
    def Tzadatak_ciklus(self,d,U,eta,v,I,T0,T0_1,T0_2,T0_3,T0_4,y1,y2,y3,rez_x,rez_y,Thl1,Thl2,Thl3,Thl4,rho,cp,la):

        c=cp
        a2=la/(rho*c)

        tau=200

        tau = np.linspace(0.001, 150, int(rez_x), endpoint = True)

        q=U*I*eta

        T1y1 = ( q / ( v * d * ( np.sqrt( 4 * np.pi * la * rho * c * tau ) ) ) ) * np.exp( - ( y1**2 ) / ( 4 * a2 * tau ) ) + T0_1
        T1y2 = ( q / ( v * d * ( np.sqrt( 4 * np.pi * la * rho * c * tau ) ) ) ) * np.exp( - ( y2**2 ) / ( 4 * a2 * tau ) ) + T0_1
        T1y3 = ( q / ( v * d * ( np.sqrt( 4 * np.pi * la * rho * c * tau ) ) ) ) * np.exp( - ( y3**2 ) / ( 4 * a2 * tau ) ) + T0_1
        T2y1 = ( q / ( v * d * ( np.sqrt( 4 * np.pi * la * rho * c * tau ) ) ) ) * np.exp( - ( y1**2 ) / ( 4 * a2 * tau ) ) + T0_2
        T2y2 = ( q / ( v * d * ( np.sqrt( 4 * np.pi * la * rho * c * tau ) ) ) ) * np.exp( - ( y2**2 ) / ( 4 * a2 * tau ) ) + T0_2
        T2y3 = ( q / ( v * d * ( np.sqrt( 4 * np.pi * la * rho * c * tau ) ) ) ) * np.exp( - ( y3**2 ) / ( 4 * a2 * tau ) ) + T0_2
        T3y1 = ( q / ( v * d * ( np.sqrt( 4 * np.pi * la * rho * c * tau ) ) ) ) * np.exp( - ( y1**2 ) / ( 4 * a2 * tau ) ) + T0_3
        T3y2 = ( q / ( v * d * ( np.sqrt( 4 * np.pi * la * rho * c * tau ) ) ) ) * np.exp( - ( y2**2 ) / ( 4 * a2 * tau ) ) + T0_3
        T3y3 = ( q / ( v * d * ( np.sqrt( 4 * np.pi * la * rho * c * tau ) ) ) ) * np.exp( - ( y3**2 ) / ( 4 * a2 * tau ) ) + T0_3
        T4y1 = ( q / ( v * d * ( np.sqrt( 4 * np.pi * la * rho * c * tau ) ) ) ) * np.exp( - ( y1**2 ) / ( 4 * a2 * tau ) ) + T0_4
        T4y2 = ( q / ( v * d * ( np.sqrt( 4 * np.pi * la * rho * c * tau ) ) ) ) * np.exp( - ( y2**2 ) / ( 4 * a2 * tau ) ) + T0_4
        T4y3 = ( q / ( v * d * ( np.sqrt( 4 * np.pi * la * rho * c * tau ) ) ) ) * np.exp( - ( y3**2 ) / ( 4 * a2 * tau ) ) + T0_4

                
        fig = make_subplots(rows=2, cols=2)


        fig.add_trace(go.Scatter(x=tau, y=T1y1,
                            mode='lines',
                            name=f'y01={y1}[m]'),
                              row=1, col=1)
        fig.add_trace(go.Scatter(x=tau, y=T1y2,
                            mode='lines',
                            name=f'y02={y2}[m]'),
                              row=1, col=1)
        fig.add_trace(go.Scatter(x=tau, y=T1y3,
                            mode='lines',
                            name=f'y03={y3}[m]'),
                              row=1, col=1)
        fig.add_trace(go.Scatter(x=tau, y=T2y1,
                            mode='lines',
                            name=f'y01={y1}[m]'),
                              row=1, col=2)
        fig.add_trace(go.Scatter(x=tau, y=T2y2,
                            mode='lines',
                            name=f'y02={y2}[m]'),
                              row=1, col=2)
        fig.add_trace(go.Scatter(x=tau, y=T2y3,
                            mode='lines',
                            name=f'y03={y3}[m]'),
                              row=1, col=2)
        fig.add_trace(go.Scatter(x=tau, y=T1y1,
                            mode='lines',
                            name=f'y01={y1}[m]'),
                              row=2, col=1)
        fig.add_trace(go.Scatter(x=tau, y=T1y2,
                            mode='lines',
                            name=f'y02={y2}[m]'),
                              row=2, col=1)
        fig.add_trace(go.Scatter(x=tau, y=T1y3,
                            mode='lines',
                            name=f'y03={y3}[m]'),
                              row=2, col=1)
        fig.add_trace(go.Scatter(x=tau, y=T2y1,
                            mode='lines',
                            name=f'y01={y1}[m]'),
                              row=2, col=2)
        fig.add_trace(go.Scatter(x=tau, y=T2y2,
                            mode='lines',
                            name=f'y02={y2}[m]'),
                              row=2, col=2)
        fig.add_trace(go.Scatter(x=tau, y=T2y3,
                            mode='lines',
                            name=f'y03={y3}[m]'),
                              row=2, col=2)

#U+03C4
        fig.update_layout(height=600, width=800,title_text="Temperaturni ciklus")#, title_text=u"\u03d1"+"=f(x,y) sa parametarskom vrijednošću y")
        fig.update_layout(margin=dict(l=0, r=0, t=80, b=0))

        fig.update_xaxes(title_text=u"\u03c4 [s]", row=1, col=1)
        fig.update_xaxes(title_text=u"\u03c4 [s]", row=1, col=2)
        fig.update_xaxes(title_text=u"\u03c4 [s]", row=2, col=1)
        fig.update_xaxes(title_text=u"\u03c4 [s]", row=2, col=2)
        fig.update_yaxes(title_text="Temperatura [°C]", row=1, col=1)
        fig.write_image("Tzadatak_ciklus.png")
        html2 = '<html><body>'
        html2 += plotly.offline.plot(fig, output_type='div', include_plotlyjs='cdn')
        html2 += '</body></html>'
        
        return html2, q

    def Dzadatak_2D_x(self,talj,d,q,roc,v,la,a,y1,y2,y3,y4):
        T_0=20
        x = np.linspace(-0.2, 0.01, 100, endpoint = True)
        y1m = np.full((100), y1)        
        y2m = np.full((100), y2)
        y3m = np.full((100), y3)
        y4m = np.full((100), y4)
        
        r1_1 = np.sqrt( x**2 + y1m**2 )
        r1_2 = np.sqrt( x**2 + y2m**2 )
        r1_3 = np.sqrt( x**2 + y3m**2 )
        r1_4 = np.sqrt( x**2 + y4m**2 )
        a2=la/roc
        b = 2 * a / ( roc * d )
        ARG_1_1 = ( r1_1 * ( np.sqrt( ( ( v**2 ) / ( 4 * (a2 ** 2) ) ) + ( b / a2 ) ) ) )
        ARG_1_2 = ( r1_2 * ( np.sqrt( ( ( v**2 ) / ( 4 * (a2 ** 2) ) ) + ( b / a2 ) ) ) )
        ARG_1_3 = ( r1_3 * ( np.sqrt( ( ( v**2 ) / ( 4 * (a2 ** 2) ) ) + ( b / a2 ) ) ) )
        ARG_1_4 = ( r1_4 * ( np.sqrt( ( ( v**2 ) / ( 4 * (a2 ** 2) ) ) + ( b / a2 ) ) ) )
        
        ARG_2 = ( np.exp( ( - v * x ) / ( 2 * a2 ) ) )
        K_0_1 = k0( ARG_1_1 )
        K_0_2 = k0( ARG_1_2 )
        K_0_3 = k0( ARG_1_3 )
        K_0_4 = k0( ARG_1_4 )
        
        T1_1 = ( q / ( 2 * np.pi * la * d ) ) * ARG_2 * K_0_1 + T_0
        T1_2 = ( q / ( 2 * np.pi * la * d ) ) * ARG_2 * K_0_2 + T_0
        T1_3 = ( q / ( 2 * np.pi * la * d ) ) * ARG_2 * K_0_3 + T_0
        T1_4 = ( q / ( 2 * np.pi * la * d ) ) * ARG_2 * K_0_4 + T_0

        for i in range(0,len(T1_1),1):
            if (T1_1[i]>talj):
                T1_1[i]=talj
            if (T1_2[i]>talj):
                T1_2[i]=talj
            if (T1_3[i]>talj):
                T1_3[i]=talj
            if (T1_4[i]>talj):
                T1_4[i]=talj
        
                
        fig = make_subplots(rows=1, cols=1)

        fig.add_trace(go.Scatter(x=x, y=T1_1,
                            mode='lines',
                            name=f'y1={y1}[m]'),
                              row=1, col=1)
        fig.add_trace(go.Scatter(x=x, y=T1_2,
                            mode='lines',
                            name=f'y2={y2}[m]'),
                              row=1, col=1)
        fig.add_trace(go.Scatter(x=x, y=T1_3,
                            mode='lines',
                            name=f'y3={y3}[m]'),
                              row=1, col=1)
        fig.add_trace(go.Scatter(x=x, y=T1_4,
                            mode='lines',
                            name=f'y4={y4}[m]'),
                              row=1, col=1)
        
        fig.update_layout(height=650, width=800, title_text=u"\u03d1"+"=f(x,y) sa parametarskom vrijednošću y")
        fig.update_layout(margin=dict(l=0, r=0, t=80, b=0))
        fig.update_xaxes(title_text="X [m]", row=1, col=1)
        fig.update_yaxes(title_text="Temperatura [°C]", row=1, col=1)
        fig.write_image("Dzadatak_2D_x.png")
        html2 = '<html><body>'
        html2 += plotly.offline.plot(fig, output_type='div', include_plotlyjs='cdn')
        html2 += '</body></html>'
        
        return html2,v,q,a,la
    
    def Dzadatak_2D_y(self,talj,d,q,roc,v,la,a,x1,x2,x3,x4):

        T_0=20

        y = np.linspace(-0.045, 0.045, 100, endpoint = True)
        x1m = np.full((100), x1)        
        x2m = np.full((100), x2)
        x3m = np.full((100), x3)
        x4m = np.full((100), x4)
        
        r1_1 = np.sqrt( y**2 + x1m**2 )
        r1_2 = np.sqrt( y**2 + x2m**2 )
        r1_3 = np.sqrt( y**2 + x3m**2 )
        r1_4 = np.sqrt( y**2 + x4m**2 )
        a2=la/roc
        b = 2 * a / ( roc * d )
        ARG_1_1 = ( r1_1 * ( np.sqrt( ( ( v**2 ) / ( 4 * (a2 ** 2) ) ) + ( b / a2 ) ) ) )
        ARG_1_2 = ( r1_2 * ( np.sqrt( ( ( v**2 ) / ( 4 * (a2 ** 2) ) ) + ( b / a2 ) ) ) )
        ARG_1_3 = ( r1_3 * ( np.sqrt( ( ( v**2 ) / ( 4 * (a2 ** 2) ) ) + ( b / a2 ) ) ) )
        ARG_1_4 = ( r1_4 * ( np.sqrt( ( ( v**2 ) / ( 4 * (a2 ** 2) ) ) + ( b / a2 ) ) ) )
        
        ARG_2_1 = ( np.exp( ( - v * x1m ) / ( 2 * a2 ) ) )
        ARG_2_2 = ( np.exp( ( - v * x2m ) / ( 2 * a2 ) ) )
        ARG_2_3 = ( np.exp( ( - v * x3m ) / ( 2 * a2 ) ) )
        ARG_2_4 = ( np.exp( ( - v * x4m ) / ( 2 * a2 ) ) )
        
        K_0_1 = k0( ARG_1_1 )
        K_0_2 = k0( ARG_1_2 )
        K_0_3 = k0( ARG_1_3 )
        K_0_4 = k0( ARG_1_4 )
        
        T1_1 = ( q / ( 2 * np.pi * la * d ) ) * ARG_2_1 * K_0_1 + T_0
        T1_2 = ( q / ( 2 * np.pi * la * d ) ) * ARG_2_2 * K_0_2 + T_0
        T1_3 = ( q / ( 2 * np.pi * la * d ) ) * ARG_2_3 * K_0_3 + T_0
        T1_4 = ( q / ( 2 * np.pi * la * d ) ) * ARG_2_4 * K_0_4 + T_0
        
        for i in range(0,len(T1_1),1):
            if (T1_1[i]>talj):
                T1_1[i]=talj
        for i in range(0,len(T1_1),1):
            if (T1_1[i]>talj):
                T1_1[i]=talj
            if (T1_2[i]>talj):
                T1_2[i]=talj
            if (T1_3[i]>talj):
                T1_3[i]=talj
            if (T1_4[i]>talj):
                T1_4[i]=talj
        
                
        fig = make_subplots(rows=1, cols=1)

        fig.add_trace(go.Scatter(x=y, y=T1_1,
                            mode='lines',
                            name=f'x1={x1}[m]'),
                              row=1, col=1)
        fig.add_trace(go.Scatter(x=y, y=T1_2,
                            mode='lines',
                            name=f'x2={x2}[m]'),
                              row=1, col=1)
        fig.add_trace(go.Scatter(x=y, y=T1_3,
                            mode='lines',
                            name=f'x3={x3}[m]'),
                              row=1, col=1)
        fig.add_trace(go.Scatter(x=y, y=T1_4,
                            mode='lines',
                            name=f'x4={x4}[m]'),
                              row=1, col=1)
        
        fig.update_layout(height=650, width=800, title_text=u"\u03d1"+"=f(x,y) sa parametarskom vrijednošću x")
        fig.update_layout(margin=dict(l=0, r=0, t=80, b=0))
        fig.update_xaxes(title_text="Y [m]", row=1, col=1)
        fig.update_yaxes(title_text="Temperatura [°C]", row=1, col=1)
        fig.write_image("Dzadatak_2D_y.png")
        html2 = '<html><body>'
        html2 += plotly.offline.plot(fig, output_type='div', include_plotlyjs='cdn')
        html2 += '</body></html>'
        
        return html2,v,q,a,la
               
    def zadatak_2D_x(self,v,q,talj,la,a,z1,z2,y1,y2,y3,y4):
        x1 = np.linspace(-0.2, 0.01, 100, endpoint = True)        
        z1_1 = np.full((100), z1)
        z1_2 = np.full((100), z2)

        y1m = np.full((100), y1)        
        y2m = np.full((100), y2)
        y3m = np.full((100), y3)
        y4m = np.full((100), y4)

        r1_1 = np.sqrt( x1**2 + y1m**2 + z1_1**2 )
        r2_1 = np.sqrt( x1**2 + y2m**2 + z1_1**2 )
        r3_1 = np.sqrt( x1**2 + y3m**2 + z1_1**2 )
        r4_1 = np.sqrt( x1**2 + y4m**2 + z1_1**2 )
        
        T1_1 = ( q / ( 2 * 3.14 * la * r1_1 ) ) * np.exp( - ( v / ( 2 * a ) * ( x1 + r1_1 ) ) )
        T2_1 = ( q / ( 2 * 3.14 * la * r2_1 ) ) * np.exp( - ( v / ( 2 * a ) * ( x1 + r2_1 ) ) )
        T3_1 = ( q / ( 2 * 3.14 * la * r3_1 ) ) * np.exp( - ( v / ( 2 * a ) * ( x1 + r3_1 ) ) )
        T4_1 = ( q / ( 2 * 3.14 * la * r4_1 ) ) * np.exp( - ( v / ( 2 * a ) * ( x1 + r4_1 ) ) )
        
        r1_2 = np.sqrt( x1**2 + y1m**2 + z1_2**2 )
        r2_2 = np.sqrt( x1**2 + y2m**2 + z1_2**2 )
        r3_2 = np.sqrt( x1**2 + y3m**2 + z1_2**2 )
        r4_2 = np.sqrt( x1**2 + y4m**2 + z1_2**2 )
        
        T1_2 = ( q / ( 2 * 3.14 * la * r1_2 ) ) * np.exp( - ( v / ( 2 * a ) * ( x1 + r1_2 ) ) )
        T2_2 = ( q / ( 2 * 3.14 * la * r2_2 ) ) * np.exp( - ( v / ( 2 * a ) * ( x1 + r2_2 ) ) )
        T3_2 = ( q / ( 2 * 3.14 * la * r3_2 ) ) * np.exp( - ( v / ( 2 * a ) * ( x1 + r3_2 ) ) )
        T4_2 = ( q / ( 2 * 3.14 * la * r4_2 ) ) * np.exp( - ( v / ( 2 * a ) * ( x1 + r4_2 ) ) )

        for i in range(0,len(T1_1),1):
            if (T1_1[i]>talj):
                T1_1[i]=talj
            if (T1_2[i]>talj):
                T1_2[i]=talj
            if (T2_1[i]>talj):
                T2_1[i]=talj
            if (T2_2[i]>talj):
                T2_2[i]=talj
                
        fig = make_subplots(rows=1, cols=2, subplot_titles=(f"Z1={z1}[m]", f"Z2={z2}[m]"))
        
        fig.add_trace(go.Scatter(x=x1, y=T1_1,
                            mode='lines',
                            name=f'y1_z1={y1}[m]'),
                              row=1, col=1)
        fig.add_trace(go.Scatter(x=x1, y=T2_1,
                            mode='lines',
                            name=f'y2_z1={y2}[m]'),
                              row=1, col=1)
        fig.add_trace(go.Scatter(x=x1, y=T3_1,
                            mode='lines',
                            name=f'y3_z1={y3}[m]'),
                              row=1, col=1)
        fig.add_trace(go.Scatter(x=x1, y=T4_1,
                            mode='lines',
                            name=f'y4_z1={y4}[m]'),
                              row=1, col=1)
        
        fig.add_trace(go.Scatter(x=x1, y=T1_2,
                            mode='lines',
                            name=f'y1_z2={y1}[m]'),
                              row=1, col=2)
        fig.add_trace(go.Scatter(x=x1, y=T2_2,
                            mode='lines',
                            name=f'y2_z2={y2}[m]'),
                              row=1, col=2)
        fig.add_trace(go.Scatter(x=x1, y=T3_2,
                            mode='lines',
                            name=f'y3_z2={y3}[m]'),
                              row=1, col=2)
        fig.add_trace(go.Scatter(x=x1, y=T4_2,
                            mode='lines',
                            name=f'y4_z2={y4}[m]'),
                              row=1, col=2)
        
        fig.update_layout(height=650, width=800, title_text=u"\u03d1"+"=f(x,y) sa parametarskom vrijednošću y")
        fig.update_layout(margin=dict(l=0, r=0, t=80, b=0))

        fig.update_xaxes(title_text="X [m]", row=1, col=1)
        fig.update_xaxes(title_text="X [m]", row=1, col=2)
        fig.update_yaxes(title_text="Temperatura [°C]", row=1, col=1)

        fig.write_image("zadatak_2D_x.png")

        html2 = '<html><body>'
        html2 += plotly.offline.plot(fig, output_type='div', include_plotlyjs='cdn')
        html2 += '</body></html>'
        
        return html2
    
    
    def zadatak_2D_y(self,v,q,talj,la,a,z1,z2,x1,x2,x3,x4):

        y1 = np.linspace(-0.03, 0.03, 100, endpoint = True)
        
        z1_1 = np.full((100), z1)
        z1_2 = np.full((100), z2)

        x1m = np.full((100), x1)        
        x2m = np.full((100), x2)
        x3m = np.full((100), x3)
        x4m = np.full((100), x4)
        
        r1_1 = np.sqrt( abs(x1m)**2 + y1**2 + z1_1**2 )
        r2_1 = np.sqrt( abs(x2m)**2 + y1**2 + z1_1**2 )
        r3_1 = np.sqrt( abs(x3m)**2 + y1**2 + z1_1**2 )
        r4_1 = np.sqrt( abs(x4m)**2 + y1**2 + z1_1**2 )
        T1_1 = ( q / ( 2 * 3.14 * la * r1_1 ) ) * np.exp( - ( v / ( 2 * a ) * ( x1m + r1_1 ) ) )
        T2_1 = ( q / ( 2 * 3.14 * la * r2_1 ) ) * np.exp( - ( v / ( 2 * a ) * ( x2m + r2_1 ) ) )
        T3_1 = ( q / ( 2 * 3.14 * la * r3_1 ) ) * np.exp( - ( v / ( 2 * a ) * ( x3m + r3_1 ) ) )
        T4_1 = ( q / ( 2 * 3.14 * la * r4_1 ) ) * np.exp( - ( v / ( 2 * a ) * ( x4m + r4_1 ) ) )
        
        r1_2 = np.sqrt( abs(x1m)**2 + y1**2 + z1_2**2 )
        r2_2 = np.sqrt( abs(x2m)**2 + y1**2 + z1_2**2 )
        r3_2 = np.sqrt( abs(x3m)**2 + y1**2 + z1_2**2 )
        r4_2 = np.sqrt( abs(x4m)**2 + y1**2 + z1_2**2 )
        T1_2 = ( q / ( 2 * 3.14 * la * r1_2 ) ) * np.exp( - ( v / ( 2 * a ) * ( x1m + r1_2 ) ) )
        T2_2 = ( q / ( 2 * 3.14 * la * r2_2 ) ) * np.exp( - ( v / ( 2 * a ) * ( x2m + r2_2 ) ) )
        T3_2 = ( q / ( 2 * 3.14 * la * r3_2 ) ) * np.exp( - ( v / ( 2 * a ) * ( x3m + r3_2 ) ) )
        T4_2 = ( q / ( 2 * 3.14 * la * r4_2 ) ) * np.exp( - ( v / ( 2 * a ) * ( x4m + r4_2 ) ) )
        
        for i in range(0,len(T1_1),1):
            if (T1_1[i]>talj):
                T1_1[i]=talj
            if (T2_1[i]>talj):
                T2_1[i]=talj
            if (T3_1[i]>talj):
                T3_1[i]=talj
            if (T4_1[i]>talj):
                T4_1[i]=talj
            if (T1_2[i]>talj):
                T1_2[i]=talj
            if (T2_2[i]>talj):
                T2_2[i]=talj
            if (T3_2[i]>talj):
                T3_2[i]=talj
            if (T4_2[i]>talj):
                T4_2[i]=talj
        fig = make_subplots(rows=1, cols=2, subplot_titles=(f"Z1={z1}[m]", f"Z2={z2}[m]"))

        fig.add_trace(go.Scatter(x=y1, y=T1_1,
                            mode='lines',
                            name=f'x1_z1={x1}'),
                              row=1, col=1)
        fig.add_trace(go.Scatter(x=y1, y=T2_1,
                            mode='lines',
                            name=f'x2_z1={x2}'),
                              row=1, col=1)
        fig.add_trace(go.Scatter(x=y1, y=T3_1,
                            mode='lines',
                            name=f'x3_z1={x3}'),
                              row=1, col=1)
        fig.add_trace(go.Scatter(x=y1, y=T4_1,
                            mode='lines',
                            name=f'x4_z1={x4}'),
                              row=1, col=1)
        
        fig.add_trace(go.Scatter(x=y1, y=T1_2,
                            mode='lines',
                            name=f'x1_z2={x1}'),
                              row=1, col=2)
        fig.add_trace(go.Scatter(x=y1, y=T2_2,
                            mode='lines',
                            name=f'x2_z2={x2}'),
                              row=1, col=2)
        fig.add_trace(go.Scatter(x=y1, y=T3_2,
                            mode='lines',
                            name=f'x3_z2={x3}'),
                              row=1, col=2)
        fig.add_trace(go.Scatter(x=y1, y=T4_2,
                            mode='lines',
                            name=f'x4_z2={x4}'),
                              row=1, col=2)
        
        fig.update_layout(height=650, width=800, title_text=u"\u03d1"+"=f(x,y) sa parametarskom vrijednošću x")
        fig.update_layout(margin=dict(l=0, r=0, t=80, b=0))
        fig.update_xaxes(title_text="Y [m]", row=1, col=1)
        fig.update_xaxes(title_text="Y [m]", row=1, col=2)
        fig.update_yaxes(title_text="Temperatura [°C]", row=1, col=1)

        fig.write_image("zadatak_2D_y.png")

        html2 = '<html><body>'
        html2 += plotly.offline.plot(fig, output_type='div', include_plotlyjs='cdn')
        html2 += '</body></html>'
        
        return html2,v,q,a,la
    
    def zadatak_2D_v(self,v,q,talj,la,a,z1,z2,v0,v1,v2):

        x1 = np.linspace(-0.2, 0.01, 100, endpoint = True)
        z1_1 = np.full((100), z1)
        z1_2 = np.full((100), z2)
        y1 = np.full((100), 0.015)        
     
        r1_1 = np.sqrt( x1**2 + y1**2 + z1_1**2 )
        T1_1 = ( q / ( 2 * 3.14 * la * r1_1 ) ) * np.exp( - ( v0 / ( 2 * a ) * ( x1 + r1_1 ) ) )
        T2_1 = ( q / ( 2 * 3.14 * la * r1_1 ) ) * np.exp( - ( v1 / ( 2 * a ) * ( x1 + r1_1 ) ) )
        T3_1 = ( q / ( 2 * 3.14 * la * r1_1 ) ) * np.exp( - ( v2 / ( 2 * a ) * ( x1 + r1_1 ) ) )
        
        r1_2 = np.sqrt( x1**2 + y1**2 + z1_2**2 )
        T1_2 = ( q / ( 2 * 3.14 * la * r1_2 ) ) * np.exp( - ( v0 / ( 2 * a ) * ( x1 + r1_2 ) ) )
        T2_2 = ( q / ( 2 * 3.14 * la * r1_2 ) ) * np.exp( - ( v1 / ( 2 * a ) * ( x1 + r1_2 ) ) )
        T3_2 = ( q / ( 2 * 3.14 * la * r1_2 ) ) * np.exp( - ( v2 / ( 2 * a ) * ( x1 + r1_2 ) ) )
        
        for i in range(0,len(T1_1),1):
            if (T1_1[i]>talj):
                T1_1[i]=talj
            if (T1_2[i]>talj):
                T1_2[i]=talj
            if (T2_1[i]>talj):
                T2_1[i]=talj
            if (T2_2[i]>talj):
                T2_2[i]=talj
        fig = make_subplots(rows=1, cols=2, subplot_titles=(f"Z1={z1}[m]", f"Z2={z2}[m]"))

        fig.add_trace(go.Scatter(x=x1, y=T1_1,
                            mode='lines',
                            name=f'v0_z1={v0}'),
                              row=1, col=1)
        fig.add_trace(go.Scatter(x=x1, y=T2_1,
                            mode='lines',
                            name=f'v1_z1={v1}'),
                              row=1, col=1)
        fig.add_trace(go.Scatter(x=x1, y=T3_1,
                            mode='lines',
                            name=f'v2_z1={v2}'),
                              row=1, col=1)

        fig.add_trace(go.Scatter(x=x1, y=T1_2,
                            mode='lines',
                            name=f'v0_z2={v0}'),
                              row=1, col=2)
        fig.add_trace(go.Scatter(x=x1, y=T2_2,
                            mode='lines',
                            name=f'v1_z2={v1}'),
                              row=1, col=2)
        fig.add_trace(go.Scatter(x=x1, y=T3_2,
                            mode='lines',
                            name=f'v2_z2={v2}'),
                              row=1, col=2)

        fig.update_layout(height=650, width=800, title_text=u"\u03d1"+"=f(x,v) sa parametarskom vrijednošću v za y=0.015[m]")
        fig.update_layout(margin=dict(l=0, r=0, t=80, b=0))
        fig.update_xaxes(title_text="X [m]", row=1, col=1)
        fig.update_xaxes(title_text="X [m]", row=1, col=2)
        fig.update_yaxes(title_text="Temperatura [°C]", row=1, col=1)

        fig.write_image("zadatak_2D_v.png")

        html2 = '<html><body>'
        html2 += plotly.offline.plot(fig, output_type='div', include_plotlyjs='cdn')
        html2 += '</body></html>'
        
        return html2,v,q,a,la

    def zadatak_3D_z1(self, gornji_x, donji_x, gornji_y, donji_y,v,q,talj,la,a,z1,rez_x,rez_y):

        y1_a=[]
        cnt=0
        
        rez_x=int(rez_x)
        rez_y=int(rez_y)
        
        rng_y = np.linspace(donji_y, gornji_y, rez_y, endpoint = True)
        
        for i in range(len(rng_y)):
            cnt+=1
            n=np.full((rez_x), rng_y[i])
            y1_a.append(n)
        y1 = np.vstack(y1_a).ravel() 
        x1_0 = np.linspace(donji_x, gornji_x, rez_x, endpoint = True)
        x1 = np.tile(x1_0, cnt)
        z1_1 = np.full((cnt*rez_x), z1)   
        r1_1 = np.sqrt( x1**2 + y1**2 + z1_1**2 )
        T1_1 = ( q / ( 2 * 3.14 * la * r1_1 ) ) * np.exp( - ( v / ( 2 * a ) * ( x1 + r1_1 ) ) )
        
        for i in range(0,len(T1_1),1):
            if (T1_1[i]>talj):
                T1_1[i]=talj
        d3_4 = np.dstack([x1,y1,T1_1])
        d3_4f=d3_4.reshape(cnt*rez_x,3)
        df = pd.DataFrame(d3_4f, columns = ['x','y','z'])

        fig = px.scatter_3d(df, x = 'x', 
                            y = 'y', 
                            z = 'z',
                            color="z")

        fig.update_layout(height=620, width=800, title_text=u"\u03d1"+"=f(x,y)"+", Z1="+str(z1)+"[m]")
        
        fig.update_layout(margin=dict(l=0, r=0, t=50, b=0),
                          coloraxis_colorbar=dict(
                          title="Temperatura [°C]"),
                          
        scene = dict(
        xaxis = dict(
            title='X[m]'),
        yaxis = dict(
            title='Y[m]'),
        zaxis = dict(
            title='Temperatura [°C]'),),)

        fig.write_image("zadatak_3D_z1.png")
        html = '<html><body>'
        html += plotly.offline.plot(fig, output_type='div', include_plotlyjs='cdn')
        html += '</body></html>'
        return html
    
    def zadatak_3D_z2(self, gornji_x, donji_x, gornji_y, donji_y,v,q,talj,la,a,z2,rez_x,rez_y):

        y1_a=[]
        cnt=0
        
        rez_x=int(rez_x)
        rez_y=int(rez_y)
              
        rng_y = np.linspace(donji_y, gornji_y, rez_y, endpoint = True)
        
        for i in range(len(rng_y)):
            cnt+=1
            n=np.full((rez_x), rng_y[i])
            y1_a.append(n)
        y1 = np.vstack(y1_a).ravel() 
        x1_0 = np.linspace(donji_x, gornji_x, rez_x, endpoint = True)
        x1 = np.tile(x1_0, cnt)
        z1_1 = np.full((cnt*rez_x), z2)   

        r1_1 = np.sqrt( x1**2 + y1**2 + z1_1**2 )
        T1_1 = ( q / ( 2 * 3.14 * la * r1_1 ) ) * np.exp( - ( v / ( 2 * a ) * ( x1 + r1_1 ) ) )
        
        for i in range(0,len(T1_1),1):
            if (T1_1[i]>talj):
                T1_1[i]=talj
        d3_4 = np.dstack([x1,y1,T1_1])
        d3_4f=d3_4.reshape(cnt*rez_x,3)
        df = pd.DataFrame(d3_4f, columns = ['x','y','z'])
        fig = px.scatter_3d(df, x = 'x', 
                            y = 'y', 
                            z = 'z',
                            color="z")
        fig.update_layout(height=620, width=800, title_text=u"\u03d1"+"=f(x,y)"+", Z2="+str(z2)+"[m]")
        
        fig.update_layout(margin=dict(l=0, r=0, t=50, b=0),
                          coloraxis_colorbar=dict(
                          title="Temperatura [°C]"),
                          
        scene = dict(
        xaxis = dict(
            title='X[m]'),
        yaxis = dict(
            title='Y[m]'),
        zaxis = dict(
            title='Temperatura [°C]'),),)
        fig.write_image("zadatak_3D_z2.png")
        html = '<html><body>'
        html += plotly.offline.plot(fig, output_type='div', include_plotlyjs='cdn')
        html += '</body></html>'
        return html

    def initUI(self):

        self.pushButton_5.clicked.connect(self.analiziram)
        self.pushButton_30.clicked.connect(self.prva_analiza)
        self.pushButton_3.clicked.connect(self.druga_analiza)
        self.pushButton_7.clicked.connect(self.primjer)
        self.pushButton_9.clicked.connect(self.pdf_1)
        self.pushButton_2.clicked.connect(self.home)
        self.pushButton_34.clicked.connect(self.Dprimjer)
        self.pushButton_37.clicked.connect(self.Danaliziram)
        self.pushButton_25.clicked.connect(self.Tanaliziram)
        self.pushButton_16.clicked.connect(self.home)
        self.pushButton_21.clicked.connect(self.Tprimjer)
        self.pushButton_29.clicked.connect(self.druga_analiza)
        self.pushButton_23.clicked.connect(self.treca_analiza)
        self.pushButton.clicked.connect(self.home)
        self.pushButton_27.clicked.connect(self.pomoc)
        self.pushButton_20.clicked.connect(self.home)
        self.pushButton_31.clicked.connect(self.pdf_2)
        self.pushButton_17.clicked.connect(self.pdf_3)
        self.pushButton_26.clicked.connect(self.oprogramu)
        self.pushButton_20.clicked.connect(self.home)
        self.pushButton_8.clicked.connect(self.pomoc)
        self.pushButton_19.clicked.connect(self.prva_analiza)
        self.pushButton_10.clicked.connect(self.druga_analiza)
        self.pushButton_11.clicked.connect(self.treca_analiza)
        self.pushButton_28.clicked.connect(self.oprogramu)
        self.pushButton_39.clicked.connect(self.home)
        self.pushButton_79.clicked.connect(self.prva_analiza)
        self.pushButton_35.clicked.connect(self.druga_analiza)
        self.pushButton_36.clicked.connect(self.treca_analiza)
        self.pushButton_4.clicked.connect(self.treca_analiza)
        self.pushButton_6.clicked.connect(self.pomoc)
        self.pushButton_12.clicked.connect(self.oprogramu)
        self.pushButton_38.clicked.connect(self.prva_analiza)
        self.pushButton_32.clicked.connect(self.treca_analiza)
        self.pushButton_18.clicked.connect(self.pomoc)
        self.pushButton_15.clicked.connect(self.oprogramu)
        self.pushButton_33.clicked.connect(self.prva_analiza)
        self.pushButton_24.clicked.connect(self.druga_analiza)
        self.pushButton_13.clicked.connect(self.pomoc)
        self.pushButton_14.clicked.connect(self.oprogramu)
        self.pushButton_41.clicked.connect(self.pomocf)
        self.pushButton_43.clicked.connect(self.pomoc)
        self.pushButton_45.clicked.connect(self.home)
        self.pushButton_80.clicked.connect(self.prva_analiza)
        self.pushButton_42.clicked.connect(self.druga_analiza)
        self.pushButton_44.clicked.connect(self.treca_analiza)
        self.pushButton_40.clicked.connect(self.oprogramu)
    def oprogramu(self):
        print("oprogramu")
        self.stackedWidget.setCurrentWidget(self.Oprogramu)

    def pomoc(self):
        print("pomoc")
        self.stackedWidget.setCurrentWidget(self.Pomoc)

    def pomocf(self):
        print("pomocf")
        self.stackedWidget.setCurrentWidget(self.Pomoc_f)

    def treca_analiza(self):
        print("treca_analiza")
        self.stackedWidget.setCurrentWidget(self.Treca_analiza)

    def druga_analiza(self):
        print("druga_analiza")
        self.stackedWidget.setCurrentWidget(self.Druga_analiza)


    def home(self):
        print("home")
        self.stackedWidget.setCurrentWidget(self.Home)
        

    def prva_analiza(self):
        print("prva_analiza")
        self.stackedWidget.setCurrentWidget(self.Prva_analiza)
        
    def primjer(self):
        self.lineEdit.setText("0.01")
        self.lineEdit_4.setText("-0.2")  
        self.lineEdit_2.setText("0.03")  
        self.lineEdit_5.setText("-0.03")
        self.lineEdit_7.setText("0.005") 
        self.lineEdit_9.setText("25") 
        self.lineEdit_11.setText("0.000005") 
        self.lineEdit_12.setText("5000") 
        self.lineEdit_13.setText("1500") 
        self.lineEdit_3.setText("0") 
        self.lineEdit_14.setText("0.002") 
        self.lineEdit_20.setText("0") 
        self.lineEdit_22.setText("-0.015") 
        self.lineEdit_19.setText("-0.030") 
        self.lineEdit_21.setText("-0.045") 
        self.lineEdit_8.setText("0") 
        self.lineEdit_16.setText("0.005") 
        self.lineEdit_17.setText("0.010") 
        self.lineEdit_18.setText("0.015") 
        self.lineEdit_10.setText("0.0025") 
        self.lineEdit_15.setText("0.0075")
        self.lineEdit_6.setText("150") 
        self.lineEdit_23.setText("20") 
        print("primjer")
        
    def Dprimjer(self):
        self.lineEdit_41.setText("1500")
        self.lineEdit_47.setText("0.002")
        self.lineEdit_26.setText("0.005")
        self.lineEdit_26.setText("0.005")
        self.lineEdit_40.setText("3000")
        self.lineEdit_33.setText("5000000")
        self.lineEdit_39.setText("40")
        self.lineEdit_63.setText("20")
        #Y parametri
        self.lineEdit_27.setText("0") 
        self.lineEdit_46.setText("-0.05") 
        self.lineEdit_35.setText("-0.10") 
        self.lineEdit_34.setText("-0.15")
        #X parametri
        self.lineEdit_44.setText("0") 
        self.lineEdit_28.setText("0.005") 
        self.lineEdit_24.setText("0.01") 
        self.lineEdit_25.setText("0.015") 

        print("Dprimjer")
        
    def Tprimjer(self):
        self.lineEdit_57.setText("0.002")
        self.lineEdit_58.setText("28")
        self.lineEdit_45.setText("0.8")
        self.lineEdit_48.setText("0.004")
        self.lineEdit_37.setText("120")
        self.lineEdit_60.setText("20")
        self.lineEdit_31.setText("20")
        self.lineEdit_56.setText("150")
        self.lineEdit_49.setText("200") 
        self.lineEdit_55.setText("250") 
        self.lineEdit_42.setText("0.005") 
        self.lineEdit_53.setText("0.01")
        self.lineEdit_61.setText("0.015") 
        self.lineEdit_59.setText("100") 
        self.lineEdit_52.setText("100") 
        self.lineEdit_32.setText("800") 
        self.lineEdit_62.setText("700") 
        self.lineEdit_51.setText("600") 
        self.lineEdit_50.setText("500") 
        self.lineEdit_54.setText("7850") 
        self.lineEdit_64.setText("461") 
        self.lineEdit_65.setText("42.7") 

        print("Tprimjer")

    def unos(self):
        a = float(self.lineEdit_11.text())
        la = float(self.lineEdit_9.text())
        talj = float(self.lineEdit_13.text())
        gornji_x = float(self.lineEdit.text())
        donji_x  = float(self.lineEdit_4.text())
        gornji_y = float(self.lineEdit_2.text())
        donji_y  = float(self.lineEdit_5.text())
        q  = float(self.lineEdit_12.text())
        z1 = float(self.lineEdit_3.text())
        z2 = float(self.lineEdit_14.text())
        y1 = float(self.lineEdit_8.text())
        y2 = float(self.lineEdit_16.text()) 
        y3 = float(self.lineEdit_17.text()) 
        y4 = float(self.lineEdit_18.text())
        x1 = float(self.lineEdit_20.text())
        x2 = float(self.lineEdit_22.text()) 
        x3 = float(self.lineEdit_19.text()) 
        x4 = float(self.lineEdit_21.text())
        v0 = float(self.lineEdit_10.text())
        v1 = float(self.lineEdit_7.text())
        v2 = float(self.lineEdit_15.text())
        rez_x=float(self.lineEdit_6.text())
        rez_y=float(self.lineEdit_23.text())
        
        return a,la,talj,q,gornji_x,donji_x,gornji_y,donji_y,z1,z2,y1,y2,y3,y4,x1,x2,x3,x4,v0,v1,v2,rez_x,rez_y

    def Dunos(self):
        talj  = float(self.lineEdit_41.text())
        d = float(self.lineEdit_47.text())
        q = float(self.lineEdit_40.text())
        roc = float(self.lineEdit_33.text())
        v = float(self.lineEdit_26.text())
        la = float(self.lineEdit_39.text())
        a = float(self.lineEdit_63.text())
        x1 = float(self.lineEdit_27.text())
        x2 = float(self.lineEdit_46.text())
        x3 = float(self.lineEdit_35.text())
        x4 = float(self.lineEdit_34.text())
        y1 = float(self.lineEdit_44.text())
        y2 = float(self.lineEdit_28.text())
        y3 = float(self.lineEdit_24.text())
        y4 = float(self.lineEdit_25.text())

        
       
        return talj,d,q,roc,v,la,a,y1,y2,y3,y4,x1,x2,x3,x4

    def Tunos(self):
        
         d = float(self.lineEdit_57.text())
         U = float(self.lineEdit_58.text())
         eta = float(self.lineEdit_45.text())
         v = float(self.lineEdit_48.text())
         I = float(self.lineEdit_37.text())
         T0 = float(self.lineEdit_60.text())
         T0_1 = float(self.lineEdit_31.text())
         T0_2 = float(self.lineEdit_56.text())
         T0_3 = float(self.lineEdit_49.text())
         T0_4 = float(self.lineEdit_55.text())
         y1 = float(self.lineEdit_42.text())
         y2 = float(self.lineEdit_53.text())
         y3 = float(self.lineEdit_61.text())
         rez_x = float(self.lineEdit_59.text())
         rez_y = float(self.lineEdit_52.text())
         Thl1 = float(self.lineEdit_32.text())
         Thl2 = float(self.lineEdit_62.text())
         Thl3 = float(self.lineEdit_51.text())
         Thl4 = float(self.lineEdit_50.text())       
         rho = float(self.lineEdit_54.text())
         cp = float(self.lineEdit_64.text())
         la = float(self.lineEdit_65.text()) 
       
         return d,U,eta,v,I,T0,T0_1,T0_2,T0_3,T0_4,y1,y2,y3,rez_x,rez_y,Thl1,Thl2,Thl3,Thl4,rho,cp,la       

    def analiziram(self):

        i=0
        j=0
        for x in (self.lineEdit, 
                    self.lineEdit_4, 
                    self.lineEdit_2,
                    self.lineEdit_3, 
                    self.lineEdit_5,
                    self.lineEdit_6,
                    self.lineEdit_7,
                    self.lineEdit_8,
                    self.lineEdit_9,
                    self.lineEdit_10,
                    self.lineEdit_11,
                    self.lineEdit_12,
                    self.lineEdit_13,
                    self.lineEdit_14,
                    self.lineEdit_15,
                    self.lineEdit_16,
                    self.lineEdit_17,
                    self.lineEdit_18,
                    self.lineEdit_20,
                    self.lineEdit_22,
                    self.lineEdit_19,
                    self.lineEdit_21,
                    self.lineEdit_23):
            i+=1

            if len(x.text()) == 0:

                print("Svi inputi trebaju biti popunjeni")

                x.setStyleSheet("background-color: red;")


            else:
                x.setStyleSheet("background-color: #b3ff66;")
                j+=1
                
        #svaki put kad dodas novi inline, povecati j !        
        if (j==23):

            a,la,talj,q,gornji_x,donji_x,gornji_y,donji_y,z1,z2,y1,y2,y3,y4,x1,x2,x3,x4,v0,v1,v2,rez_x,rez_y = self.unos()

            print("Analiziram")
            v = v1
            
            html2 = self.zadatak_3D_z1(gornji_x,donji_x,gornji_y,donji_y,v,q,talj,la,a,z1,rez_x,rez_y)
            html3 = self.zadatak_3D_z2(gornji_x,donji_x,gornji_y,donji_y,v,q,talj,la,a,z2,rez_x,rez_y)
            html = self.zadatak_2D_x(v,q,talj,la,a,z1,z2,y1,y2,y3,y4)
            html_y = self.zadatak_2D_y(v,q,talj,la,a,z1,z2,x1,x2,x3,x4)[0]
            html_v = self.zadatak_2D_v(v,q,talj,la,a,z1,z2,v0,v1,v2)[0]
            self.tab.setHtml(html)
            self.tab_2.setHtml(html2)
            self.tab_3.setHtml(html_y)
            self.tab_4.setHtml(html_v)
            self.tab_5.setHtml(html3)
            j=0
 
    def Danaliziram(self):
        i=0
        j=0
        for x in (self.lineEdit_41,
                self.lineEdit_47,
                self.lineEdit_40,
                self.lineEdit_33,
                self.lineEdit_26,
                self.lineEdit_39,
                self.lineEdit_63,
                self.lineEdit_27,
                self.lineEdit_46,
                self.lineEdit_35,
                self.lineEdit_34,
                self.lineEdit_44,
                self.lineEdit_28,
                self.lineEdit_24,
                self.lineEdit_25):
            

            i+=1

            if len(x.text()) == 0:

                print("Svi inputi trebaju biti popunjeni")

                x.setStyleSheet("background-color: red;")

            else:
                x.setStyleSheet("background-color: #b3ff66;")
                j+=1
                
        #svaki put kad dodas novi inline, povecati j !        
        if (j==15):

            talj,d,q,roc,v,la,a,y1,y2,y3,y4,x1,x2,x3,x4 = self.Dunos()

            print("DAnaliziram")
            
            html = self.Dzadatak_2D_x(talj,d,q,roc,v,la,a,y1,y2,y3,y4)[0]
            html_y = self.Dzadatak_2D_y(talj,d,q,roc,v,la,a,x1,x2,x3,x4)[0]
            self.tab_6.setHtml(html)
            self.tab_7.setHtml(html_y)
            j=0
            
    def Tanaliziram(self):

        i=0
        j=0
        for x in (self.lineEdit_57,
                self.lineEdit_58,
                self.lineEdit_45,
                self.lineEdit_48,
                self.lineEdit_37,
                self.lineEdit_60,
                self.lineEdit_31,
                self.lineEdit_56,
                self.lineEdit_49,
                self.lineEdit_55,
                self.lineEdit_42,
                self.lineEdit_53,
                self.lineEdit_61,
                self.lineEdit_59,
                self.lineEdit_52,
                self.lineEdit_32,
                self.lineEdit_62,
                self.lineEdit_51,
                self.lineEdit_50,
                self.lineEdit_54,
                self.lineEdit_64,
                self.lineEdit_65):
            

            i+=1
            if len(x.text()) == 0:

                print("Svi inputi trebaju biti popunjeni")

                x.setStyleSheet("background-color: red;")

            else:
                x.setStyleSheet("background-color: #b3ff66;")
                j+=1
                
        #svaki put kad dodas novi inline, povecati j !        
        if (j==22):

            d,U,eta,v,I,T0,T0_1,T0_2,T0_3,T0_4,y1,y2,y3,rez_x,rez_y,Thl1,Thl2,Thl3,Thl4,rho,cp,la = self.Tunos()


            #1.
            print("TAnaliziram")
            html = self.Tzadatak_ciklus(d,U,eta,v,I,T0,T0_1,T0_2,T0_3,T0_4,y1,y2,y3,rez_x,rez_y,Thl1,Thl2,Thl3,Thl4,rho,cp,la)[0]
            q3=self.Tzadatak_ciklus(d,U,eta,v,I,T0,T0_1,T0_2,T0_3,T0_4,y1,y2,y3,rez_x,rez_y,Thl1,Thl2,Thl3,Thl4,rho,cp,la)[1]
            self.tab_8.setHtml(html)
            #2.
            html = self.Tzadatak_brzina_hl(d,U,eta,v,I,T0,T0_1,T0_2,T0_3,T0_4,y1,y2,y3,rez_x,rez_y,Thl1,Thl2,Thl3,Thl4,rho,cp,la)[0]
            q3=self.Tzadatak_brzina_hl(d,U,eta,v,I,T0,T0_1,T0_2,T0_3,T0_4,y1,y2,y3,rez_x,rez_y,Thl1,Thl2,Thl3,Thl4,rho,cp,la)[1]
            self.tab_9.setHtml(html)
            #3
            html = self.Tzadatak_vrijeme_hl(d,U,eta,v,I,T0,T0_1,T0_2,T0_3,T0_4,y1,y2,y3,rez_x,rez_y,Thl1,Thl2,Thl3,Thl4,rho,cp,la)[0]
            q3=self.Tzadatak_vrijeme_hl(d,U,eta,v,I,T0,T0_1,T0_2,T0_3,T0_4,y1,y2,y3,rez_x,rez_y,Thl1,Thl2,Thl3,Thl4,rho,cp,la)[1]
            self.tab_10.setHtml(html)
            #3 graf
            html = self.Tzadatak_vrijeme_E(d,U,eta,v,I,T0,T0_1,T0_2,T0_3,T0_4,y1,y2,y3,rez_x,rez_y,Thl1,Thl2,Thl3,Thl4,rho,cp,la)[0]
            q3=self.Tzadatak_vrijeme_hl(d,U,eta,v,I,T0,T0_1,T0_2,T0_3,T0_4,y1,y2,y3,rez_x,rez_y,Thl1,Thl2,Thl3,Thl4,rho,cp,la)[1]
            self.tab_11.setHtml(html)
            #max Temp
            html = self.Tzadatak_max_Temp(d,U,eta,v,I,T0,T0_1,T0_2,T0_3,T0_4,y1,y2,y3,rez_x,rez_y,Thl1,Thl2,Thl3,Thl4,rho,cp,la)[0]
            q3=self.Tzadatak_max_Temp(d,U,eta,v,I,T0,T0_1,T0_2,T0_3,T0_4,y1,y2,y3,rez_x,rez_y,Thl1,Thl2,Thl3,Thl4,rho,cp,la)[1]
            self.tab_13.setHtml(html)
            #ZUT
            html = self.Tzadatak_sirina_ZUT(d,U,eta,v,I,T0,T0_1,T0_2,T0_3,T0_4,y1,y2,y3,rez_x,rez_y,Thl1,Thl2,Thl3,Thl4,rho,cp,la)[0]
            q3=self.Tzadatak_sirina_ZUT(d,U,eta,v,I,T0,T0_1,T0_2,T0_3,T0_4,y1,y2,y3,rez_x,rez_y,Thl1,Thl2,Thl3,Thl4,rho,cp,la)[1]
            self.tab_12.setHtml(html)



def main():
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()