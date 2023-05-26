"""picturesque URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from picturesqueapp.views import *

from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index,name="index"),
	path('index/',index,name="index"),
    path('chome/',chome,name="chome"),
    path('adminhome/',adminhome,name="adminhome"),
    path('arthome/',arthome,name="arthome"),

    path('cusreg/',cusreg,name="cusreg"),                 #Registration
    path('cusregact/',cusregact,name="cusregact"),
    path('artreg/',artreg,name="artreg"),                 
    path('artregact/',artregact,name="artregact"),

    path('login/',login,name="login"),                    #login
    path('logout/',logout,name="logout"),                    
    path('logact/',logact,name="logact"),

    path('postimg/',postimg,name="postimg"),
    path('myimg/',myimg,name="myimg"),
    path('vimg/',vimg,name="vimg"),
    path('prv/',prv,name="prv"),
    path('delpic/',delpic,name="delpic"),
    path('vimg1/',vimg1,name="vimg1"),
    
    path('vusers/',vusers,name="vusers"),
    path('unblkuser/',unblkuser,name="unblkuser"),
    path('blkuser/',blkuser,name="blkuser"),
    path('vartist/',vartist,name="vartist"),
    path('blkart/',blkart,name="blkart"),
    path('unblkart/',unblkart,name="unblkart"),

    path('like/',like,name="like"),
    path('dislike/',dislike,name="dislike"),

    path('travel/',travel,name="travel"),
    path('mytravel/',mytravel,name="mytravel"),
    path('travelact/',travelact,name="travelact"),
    path('postimgact/',postimgact,name="postimgact"),

    path('reqa/',reqa,name="reqa"),                           #Request Auction
    path('vauction/',vauction,name="vauction"),
    path('aucaccept/',aucaccept,name="aucaccept"),
    path('aucreject/',aucreject,name="aucreject"),
    path('aucacceptact/',aucacceptact,name="aucacceptact"),
    path('aucrejectact/',aucrejectact,name="aucrejectact"),

    path('myauction/',myauction,name="myauction"),            #artist auction
    path('addbamt/',addbamt,name="addbamt"),
    path('addbamtact/',addbamtact,name="addbamtact"),
    path('vbiding/',vbiding,name="vbiding"),

    path('uauction/',uauction,name="uauction"),               #User Bid
    path('bidamt/',bidamt,name="bidamt"),
    path('bidamtact/',bidamtact,name="bidamtact"),
    path('pay/',pay,name="pay"),
    path('payact/',payact,name="payact"),

    path('vresult/',vresult,name="vresult"),

    path('bookart/',bookart,name="bookart"),                  #booking
    path('bookartact/',bookartact,name="bookartact"),
    path('mybooking/',mybooking,name="mybooking"),
    path('bkupdate/',bkupdate,name="bkupdate"),
    path('bkupdateact/',bkupdateact,name="bkupdateact"),
    path('bkdelete/',bkdelete,name="bkdelete"),

    path('bookingreq/',bookingreq,name="bookingreq"),         #booking request
    path('bkaccept/',bkaccept,name="bkaccept"),
    path('bkreject/',bkreject,name="bkreject"),

    path('bidupdate/',bidupdate,name="bidupdate"),
    path('delbid/',delbid,name="delbid"),

    path('sale/',sale,name="sale"),             #Sale
    path('buy/',buy,name="buy"),  
    path('buyaction/',buyaction,name="buyaction"), 
    path('myorders/',myorders,name="myorders"), 
    path('vorder/',vorder,name="vorder"), 
    path('ostat/',ostat,name="ostat"), 
    

    




]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()

