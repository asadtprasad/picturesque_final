from django.shortcuts import render
from django.http import HttpResponse
# from django.shortcuts import render,HttpResponseRedirect,render_to_response,redirect
from django.db import connection
from picturesqueapp.forms import pform
from picturesqueapp.models import pmodel
import datetime
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
	return render(request,'index.html')
def login(request):
	return render(request,'login.html')
def cusreg(request):
	return render(request,'cusreg.html')
def artreg(request):
	return render(request,'artreg.html')

def chome(request):
	return render(request,'userhome.html')
def arthome(request):
	return render(request,'arthome.html')
def adminhome(request):
	return render(request,'adminhome.html')

def travel(request):
	return render(request,'travel.html')

def logact(request):
    cursor=connection.cursor()
    un=request.GET['uname']
    up=request.GET['upass']
    sql8="select *from tbl_login where uname='%s' and upass='%s' and status <> 'pending' "%(un,up)
    cursor.execute(sql8)
    if(cursor.rowcount)>0:
        rs=cursor.fetchall()
        for row in rs:
            request.session['uid']=row[0]
            request.session['utype']=row[3]
        if(request.session['utype']=='admin'):
            return render(request,'adminhome.html')
        if(request.session['utype']=='artist'):
            return render(request,'arthome.html')
        if(request.session['utype']=='user'):
            return render(request,'userhome.html')
    else:
        msg="<script>alert('failed');window.location='/login/';</script>"
        return HttpResponse(msg)

def logout(request):
	try:
		del request.session['uid']
		del request.session['utype']
	except:
		pass
	return HttpResponse("<script>alert('you are loged out');window.location='/login/';</script>")

def myimg(request):
    uid=request.session['uid']
    cur=connection.cursor()
    s="select * from tbl_photo where uid=%s"%(uid)
    cur.execute(s)
    rs=cur.fetchall()
    pic=[]
    for row in rs:
        w={'phid':row[0],'uid':row[1],'img':row[2],'likes':row[3],'state':row[4],'tags':row[5]}
        pic.append(w)
    s="select wrkid,amt from tbl_sale where uid=%s"%(uid)
    cur.execute(s)
    rs=cur.fetchall()
    sl=[]
    for row in rs:
        w={'wrkid':row[0],'amt':row[1]}
        sl.append(w)
    return render(request,'myimg.html',{'uid':uid,'pic':pic,'sl':sl})

def mytravel(request):
    uid=request.session['uid']
    cur=connection.cursor()
    s="select * from tbl_travel where uid=%s"%(uid)
    cur.execute(s)
    rs=cur.fetchall()
    pic=[]
    for row in rs:
        w={'trid':row[0],'loc':row[1],'tdate':row[2],'dtls':row[3],'uid':row[4]}
        pic.append(w)
    return render(request,'mytravel.html',{'uid':uid,'pic':pic})

def vimg(request):
    uid=request.session['uid']
    cur=connection.cursor()
    s="select * from tbl_photo where state='public' and uid!=%s"%(uid)
    cur.execute(s)
    rs=cur.fetchall()
    pic=[]
    for row in rs:
        w={'phid':row[0],'uid':row[1],'img':row[2],'likes':row[3],'state':row[4],'tags':row[5]}
        pic.append(w)
    s="select wrkid,amt from tbl_sale "
    cur.execute(s)
    rs=cur.fetchall()
    sl=[]
    for row in rs:
        w={'wrkid':row[0],'amt':row[1]}
        sl.append(w)
    print(sl)
    return render(request,'vimg.html',{'uid':uid,'pic':pic,'sl':sl})

def delpic(request):
    cur=connection.cursor()
    uid=request.session['uid']
    id=request.GET['id']
    s="delete from tbl_photo where phid=%s"%(id)
    cur.execute(s)
    s="select * from tbl_photo where uid=%s"%(uid)
    cur.execute(s)
    rs=cur.fetchall()
    pic=[]
    for row in rs:
        w={'phid':row[0],'uid':row[1],'img':row[2],'likes':row[3],'state':row[4],'tags':row[5]}
        pic.append(w)
    return render(request,'myimg.html',{'uid':uid,'pic':pic})

def vimg1(request):
    uid=request.session['uid']
    cur=connection.cursor()
    sr="%"+request.GET['ss']+"%"
    s="select * from tbl_photo where state='public' and tags like '%s' and uid!=%s"%(sr,uid)
    cur.execute(s)
    rs=cur.fetchall()
    pic=[]
    for row in rs:
        w={'phid':row[0],'uid':row[1],'img':row[2],'likes':row[3],'state':row[4],'tags':row[5]}
        pic.append(w)
    return render(request,'vimg.html',{'uid':uid,'pic':pic})

def vusers(request):
    
    cur=connection.cursor()
    s="select * from tbl_cusreg,tbl_login where tbl_cusreg.rid=tbl_login.uid and tbl_login.utype = 'user' "
    cur.execute(s)
    rs=cur.fetchall()
    pic=[]
    for row in rs:
        w={'rid':row[0],'name':row[1],'address':row[2],'phno':row[3],'email':row[4],'location':row[5],'gender':row[5],'status':row[12]}
        pic.append(w)
    return render(request,'vusers.html',{'pic':pic})

def blkuser(request):
    cur=connection.cursor()
    uid=request.GET['uid']
    s1="update tbl_login set status='pending' where utype='user' and uid=%s"%(uid)
    cur.execute(s1)
    msg="<script>window.location='/vusers/';</script>"
    return HttpResponse(msg)

def unblkuser(request):
    cur=connection.cursor()
    uid=request.GET['uid']
    s1="update tbl_login set status='accepted' where utype='user' and uid=%s"%(uid)
    cur.execute(s1)
    msg="<script>window.location='/vusers/';</script>"
    return HttpResponse(msg)

def vartist(request):
    
    cur=connection.cursor()
    s="select * from tbl_cusreg,tbl_login where tbl_cusreg.rid=tbl_login.uid and tbl_login.utype='artist'"
    cur.execute(s)
    rs=cur.fetchall()
    pic=[]
    for row in rs:
        w={'rid':row[0],'name':row[1],'address':row[2],'phno':row[3],'email':row[4],'location':row[5],'gender':row[5],'status':row[12]}
        pic.append(w)
    return render(request,'vartist.html',{'pic':pic})

def blkart(request):
    cur=connection.cursor()
    uid=request.GET['uid']
    s1="update tbl_login set status='pending' where utype='artist' and uid=%s"%(uid)
    cur.execute(s1)
    msg="<script>window.location='/vartist/';</script>"
    return HttpResponse(msg)

def unblkart(request):
    cur=connection.cursor()
    uid=request.GET['uid']
    s1="update tbl_login set status='accepted' where utype='artist' and uid=%s"%(uid)
    cur.execute(s1)
    msg="<script>window.location='/vartist/';</script>"
    return HttpResponse(msg)

def postimg(request):
    uid=request.session['uid']
    return render(request,'postimg.html',{'uid':uid})

def pay(request):
    uid=request.session['uid']
    aid=request.GET['aid']
    amt=request.GET['amt']
    return render(request,'pay.html',{'uid':uid,'aid':aid,'amt':amt})

def payact(request):
    uid=request.session['uid']
    aid=request.GET['aid']
    cursor=connection.cursor()
    cursor.execute("update tbl_auction set pstatus='Paid',bidto=%s where aucid=%s"%(uid,aid))
    msg="<script>window.location='/chome/';</script>"
    return HttpResponse(msg)

def like(request):
    cur=connection.cursor()
    uid=request.session['uid']
    pid=request.GET['pid']
    lk=0
    s="select * from tbl_lcount where uid=%s and phid=%s"%(uid,pid)
    cur.execute(s)
    if(cur.rowcount>0):
        msg="<script>window.location='/vimg/';</script>"
        return HttpResponse(msg)
    else:
        s="select likes from tbl_photo where phid=%s"%(pid)
        cur.execute(s)
        rs=cur.fetchall()
        for row in rs:
            lk=int(row[0])
        lk=lk+1  
        s1="update tbl_photo set likes='%s' where phid=%s"%(lk,pid)
        cur.execute(s1)
        cur.execute("insert into tbl_lcount(phid,uid) values('%s','%s')"%(pid,uid))
    s="select * from tbl_photo where state='public' and uid!=%s"%(uid)
    cur.execute(s)
    rs=cur.fetchall()
    pic=[]
    for row in rs:
        w={'phid':row[0],'uid':row[1],'img':row[2],'likes':row[3],'state':row[4],'tags':row[5]}
        pic.append(w)
    msg="<script>window.location='/vimg/';</script>"
    return HttpResponse(msg)

def prv(request):
    cur=connection.cursor()
    uid=request.session['uid']
    pid=request.GET['id']
    st=request.GET['st']
    
    
    s1="update tbl_photo set state='%s' where phid=%s"%(st,pid)
    cur.execute(s1)
    msg="<script>window.location='/myimg/';</script>"
    return HttpResponse(msg)
    

def dislike(request):
    cur=connection.cursor()
    uid=request.session['uid']
    pid=request.GET['pid']
    lk=0
    s="select * from tbl_lcount where uid=%s and phid=%s"%(uid,pid)
    cur.execute(s)
    if(cur.rowcount>0):
        msg="<script>window.location='/vimg/';</script>"
        return HttpResponse(msg)
    else:
        s="select likes from tbl_photo where phid=%s"%(pid)
        cur.execute(s)
        rs=cur.fetchall()
        for row in rs:
            lk=int(row[0])
        lk=lk-1  
        s1="update tbl_photo set likes='%s' where phid=%s"%(lk,pid)
        cur.execute(s1)
        cur.execute("insert into tbl_lcount(phid,uid) values('%s','%s')"%(pid,uid))
    s="select * from tbl_photo where state='public' and uid!=%s"%(uid)
    cur.execute(s)
    rs=cur.fetchall()
    pic=[]
    for row in rs:
        w={'phid':row[0],'uid':row[1],'img':row[2],'likes':row[3],'state':row[4],'tags':row[5]}
        pic.append(w)
    msg="<script>window.location='/vimg/';</script>"
    return HttpResponse(msg)

def postimgact(request):
    if request.method == "POST": 
        MyProfileForm = pform(request.POST, request.FILES)
        if MyProfileForm.is_valid():
            profile = pmodel()
            profile.uid = request.POST["uid"]
            profile.state = request.POST["st"]
            profile.tags = request.POST["tags"]
            profile.img = MyProfileForm.cleaned_data["img"]
            profile.save()
            html = "<script>alert('successfully added! ');window.location='/arthome/';</script>"
            saved = True
            
        else:
            #print  request.method
            MyProfileForm = pform()
            html= "<script>alert('Try Again! ');window.location='/chome/';</script>"
    return HttpResponse(html)


def cusregact(request):
    cursor=connection.cursor()
    n=request.GET['name']
    adr=request.GET['addr']
    gnd=request.GET['gender']
    pn=request.GET['number']
    em=request.GET['email']
    loc=request.GET['loc']
    pa=request.GET['pas']
    us=request.GET['user']
    s="select * from tbl_cusreg where email='%s'"%em
    cursor.execute(s)
    if(cursor.rowcount>0):
        msg="<script>alert('Email Already Exists');window.location='/sreg/';</script>"
    else:
        sql="insert into tbl_cusreg(name,address,gender,phno,email,location,utype) values('%s','%s','%s','%s','%s','%s','%s')"%(n,adr,gnd,pn,em,loc,us)
        cursor.execute(sql)
        ss="select max(rid) from tbl_cusreg"
        cursor.execute(ss)
        rs=cursor.fetchall()
        if us == 'user':
            status='approved'
            msg="<script>alert('Successfully Registered');window.location='/login/';</script>"
        else:
            status='pending'
            msg="<script>alert('Successfully Registered!! Wait for Admin Approval!');window.location='/login/';</script>"
        for row in rs:
            sql2="insert into tbl_login(uid,uname,upass,utype,status) values('%s','%s','%s','%s','%s')"%(row[0],em,pa,us,status)
            cursor.execute(sql2)
    return HttpResponse(msg)

def artregact(request):
    cursor=connection.cursor()
    n=request.GET['name']
    adr=request.GET['addr']
    gnd=request.GET['gender']
    pn=request.GET['number']
    em=request.GET['email']
    loc=request.GET['loc']
    pa=request.GET['pas']
    s="select * from tbl_cusreg where email='%s'"%em
    cursor.execute(s)
    if(cursor.rowcount>0):
        msg="<script>alert('Email Already Exists');window.location='/sreg/';</script>"
    else:
        sql="insert into tbl_cusreg(name,address,gender,phno,email,location) values('%s','%s','%s','%s','%s','%s')"%(n,adr,gnd,pn,em,loc)
        cursor.execute(sql)
        ss="select max(rid) from tbl_cusreg"
        cursor.execute(ss)
        rs=cursor.fetchall()
        for row in rs:
            sql2="insert into tbl_login(uid,uname,upass,utype) values('%s','%s','%s','customer')"%(row[0],em,pa)
            cursor.execute(sql2)
        msg="<script>alert('success');window.location='/cusreg/';</script>"
    return HttpResponse(msg)


def travelact(request):
    cursor=connection.cursor()
    loc=request.GET['loc']
    dt=request.GET['date']
    dtls=request.GET['dtls']
 
    sql="insert into tbl_travel(loc,tdate,dtls,uid) values('%s','%s','%s','%s')"%(loc,dt,dtls,request.session['uid'])
    cursor.execute(sql)
    msg="<script>alert('Added');window.location='/mytravel/';</script>"
    return HttpResponse(msg)

def vauction(request):
    cursor=connection.cursor()
    s="SELECT * FROM tbl_auction,tbl_photo,tbl_cusreg where tbl_auction.wrkid=tbl_photo.phid and tbl_auction.uid = tbl_cusreg.rid"
    print(s)
    cursor.execute(s)
    rs=cursor.fetchall()
    list=[]
    for row in rs:
        w={'aid':row[0],'img':row[11],'artist':row[14],'amail':row[17],'bamt':row[3],'adate':row[5],'rem':row[6],'status':row[4]}
        list.append(w)
    return render(request,'vauction.html',{'list':list})

def aucaccept(request):
    aid=request.GET['aid']
    cd=datetime.datetime.today().strftime("%Y-%m-%d")
    return render(request,'aucdate.html',{'aid':aid,'now':cd})

def aucacceptact(request):
    aid=request.GET['aid']
    adate=request.GET['adate']
    rem=request.GET['rem']
    cursor=connection.cursor()
    s="update tbl_auction set adate='%s',remarks='%s',status='accepted',pstatus='Nil' where aucid = %s" %(adate,rem,aid)
    cursor.execute(s)
    msg="<script>alert('Request Accepted');window.location='/vauction/';</script>"
    return HttpResponse(msg)

def aucreject(request):
    aid=request.GET['aid']
    return render(request,'aucreject.html',{'aid':aid})

def aucrejectact(request):
    aid=request.GET['aid']
    rem=request.GET['rem']
    cursor=connection.cursor()
    s="update tbl_auction set remarks='%s',status='rejected' where aucid = %s" %(rem,aid)
    cursor.execute(s)
    msg="<script>alert('Request Rejected');window.location='/vauction/';</script>"
    return HttpResponse(msg)


def vresult(request):
    cursor=connection.cursor()
    uid=request.session['uid']
    #s="SELECT * FROM `tbl_biding` where bidtime = (SELECT MIN(bidtime) from tbl_biding where bidate =( SELECT MIN(bidate) from tbl_biding where uid IN (SELECT uid FROM `tbl_biding` where bidamt = ( SELECT MAX(bidamt) from tbl_biding GROUP BY aucid)) GROUP BY aucid)GROUP BY aucid);"
    s="SELECT tbl_biding.*,tbl_auction.baseamt,tbl_auction.status,tbl_cusreg.name,tbl_auction.bidto,tbl_auction.pstatus FROM tbl_biding,tbl_auction,tbl_cusreg WHERE tbl_auction.aucid=tbl_biding.aucid and tbl_biding.uid=tbl_cusreg.rid and tbl_auction.status='sold' and tbl_biding.status='sold';"
    cursor.execute(s)
    rs=cursor.fetchall()
    list=[]
    for row in rs:       
        w={'bidid':row[0],'aid':row[1],'bname':row[9],'bamt':row[2],'bdate':row[4],'bidtime':row[5],'status':row[6],'baseamt':row[7],'uid':row[3],'bidto':row[10],'pstatus':row[11]}
        list.append(w)
    if request.session['utype']=='admin':
        return render(request,'vresult.html',{'list':list})
    elif request.session['utype']=='artist':
        return render(request,'vresult1.html',{'list':list})
    elif request.session['utype']=='user':
        return render(request,'vresult2.html',{'list':list,'uid':uid})

def ostat(request):
    cursor=connection.cursor()
    oid=request.GET['id']
    st=request.GET['st']
    sql="update tbl_order set status='%s' where oid=%s"%(st,oid)
    cursor.execute(sql)
    msg="<script>alert('Updated');window.location='/vorder/';</script>"
    return HttpResponse(msg)

def reqa(request):
    cursor=connection.cursor()
    wid=request.GET['wid']
    sql="insert into tbl_auction(uid,wrkid,status) values('%s','%s','pending')"%(request.session['uid'],wid)
    cursor.execute(sql)
    msg="<script>alert('Successfully Requested for Auction');window.location='/myauction/';</script>"
    return HttpResponse(msg)

def sale(request):
    cursor=connection.cursor()
    wid=request.GET['wid']
    amt=request.GET['amt']
    s="select * from tbl_sale where wrkid=%s and uid=%s"%(wid,request.session['uid'])
    cursor.execute(s)
    if(cursor.rowcount>0):
        sql="update tbl_sale set amt=%s where wrkid=%s and uid=%s"%(amt,wid,request.session['uid'])
        cursor.execute(sql)
    else:
        sql="insert into tbl_sale(uid,wrkid,status,amt) values('%s','%s','pending','%s')"%(request.session['uid'],wid,amt)
        cursor.execute(sql)
    msg="<script>alert('Set for Sale');window.location='/myimg/';</script>"
    return HttpResponse(msg)

def buy(request):
    pid=request.GET['pid']
    amt=request.GET['amt']
    return render(request,'buy.html',{'pid':pid,'amt':amt})

def buyaction(request):
    cursor=connection.cursor()
    wid=request.GET['pid']
    amt=request.GET['amt']
    cd=datetime.datetime.today().strftime("%Y-%m-%d")
    uid=request.session['uid']
    sql="insert into tbl_order(wrkid,uid,odate,status) values('%s','%s','%s','pending')"%(wid,uid,cd)
    cursor.execute(sql)
    sql="update tbl_sale set status='ordered' where wrkid=%s"%(wid)
    cursor.execute(sql)
    msg="<script>alert('Ordered');window.location='/myorders/';</script>"
    return HttpResponse(msg)

def myauction(request):
    cursor=connection.cursor()
    s="select * from tbl_auction where uid=%s"%(request.session['uid'])
    cursor.execute(s)
    rs=cursor.fetchall()
    cd=datetime.datetime.today().strftime("%Y-%m-%d")
    list=[]
    for row in rs:
        w={'aid':row[0],'wrkid':row[2],'bamt':row[3],'status':row[4],'adate':row[5],'adate1':str(row[5]),'rem':row[6]}
        list.append(w)
    return render(request,'myauction.html',{'list':list,'cd':cd})

def myorders(request):
    cursor=connection.cursor()
    s="select oid,odate,tbl_order.uid,wrkid,img,tbl_order.status from tbl_order inner join tbl_photo on tbl_photo.phid=tbl_order.wrkid where tbl_order.uid=%s"%(request.session['uid'])
    cursor.execute(s)
    rs=cursor.fetchall()
    cd=datetime.datetime.today().strftime("%Y-%m-%d")
    list=[]
    for row in rs:
        w={'oid':row[0],'odate':row[1],'uid':row[2],'wrkid':row[3],'img':row[4],'status':row[5]}
        list.append(w)
    return render(request,'myorders.html',{'list':list})

def vorder(request):
    cursor=connection.cursor()
    s="select oid,odate,tbl_order.uid,wrkid,img,tbl_order.status,tbl_cusreg.name,tbl_cusreg.address,tbl_cusreg.phno,tbl_cusreg.email from tbl_order inner join tbl_photo on tbl_photo.phid=tbl_order.wrkid inner join tbl_cusreg  on tbl_cusreg.rid=tbl_order.uid where tbl_photo.uid=%s"%(request.session['uid'])
    cursor.execute(s)
    rs=cursor.fetchall()
    cd=datetime.datetime.today().strftime("%Y-%m-%d")
    list=[]
    for row in rs:
        w={'oid':row[0],'odate':row[1],'uid':row[2],'wrkid':row[3],'img':row[4],'status':row[5],'name':row[6],'adr':row[7],'phno':row[8],'email':row[9]}
        list.append(w)
    return render(request,'vorder.html',{'list':list})

def addbamt(request):
    aid=request.GET['aid']
    return render(request,'addamt.html',{'aid':aid})

def addbamtact(request):
    aid=request.GET['aid']
    amt=request.GET['amt']
    cursor=connection.cursor()
    s="update tbl_auction set baseamt='%s' where aucid = %s" %(amt,aid)
    cursor.execute(s)
    msg="<script>alert('Base Amount Updated');window.location='/myauction/';</script>"
    return HttpResponse(msg)


def uauction(request):
    cursor=connection.cursor()
    s="select * from tbl_auction where  status!='pending' and status !='rejected' "
    cursor.execute(s)
    rs=cursor.fetchall()
    list=[]
    for row in rs:
        bidamt=0
        s1="SELECT bidamt FROM tbl_biding WHERE aucid='%s' and uid= '%s'"%(row[0],request.session['uid'])
        cursor.execute(s1)
        rs1=cursor.fetchall()
        #print s1
        for row1 in rs1:
            bidamt=row1[0]
        #print(bidamt)
        w={'aid':row[0],'wrkid':row[2],'bamt':row[3],'status':row[4],'adate':row[5],'rem':row[6],'bidamt':bidamt}
        list.append(w)
    return render(request,'uauction.html',{'list':list})


def bidamt(request):
    cursor=connection.cursor()
    id=request.GET['aid']
    maxamt=0
    s="SELECT * FROM tbl_auction,tbl_photo,tbl_cusreg where tbl_auction.wrkid=tbl_photo.phid and tbl_auction.uid = tbl_cusreg.rid and tbl_auction.aucid=%s"%(id)
    cursor.execute(s)
    rs=cursor.fetchall()
    list=[]
    for row in rs:       
        w={'aid':row[0],'img':row[11],'artist':row[14],'amail':row[17],'bamt':row[3],'adate':row[5],'rem':row[6],'status':row[4]}
        list.append(w)
        maxamt=row[3]
    s1="select max(bidamt) as bidamt from tbl_biding  where aucid =%s"%(id)
    cursor.execute(s1)
    rs=cursor.fetchall()
    for row in rs:
        maxamt=row[0]

    return render(request,'bidamt.html',{'list':list,'max':maxamt})

def bidamtact(request):
    aid=request.GET['aid']
    amt=request.GET['amt']
    cd=datetime.datetime.today()
    #now_method = datetime.datetime.now()
    ti=datetime.datetime.now().strftime("%H:%M:%S")
    cursor=connection.cursor()
    s="insert into tbl_biding(aucid,bidamt,uid,bidate,bidtime,status) values('%s','%s','%s','%s','%s','bided')" %(aid,amt,request.session['uid'],cd,ti)
    cursor.execute(s)
    msg="<script>alert('Bid Amount Updated');window.location='/uauction/';</script>"
    return HttpResponse(msg)

def bookart(request):
    cursor=connection.cursor()
    phid=request.GET['pid']
    s="SELECT * FROM tbl_cusreg,tbl_photo where  tbl_photo.phid = '%s' and tbl_cusreg.rid=tbl_photo.uid"%(phid)
    cursor.execute(s)
    rs=cursor.fetchall()
    list=[]
    for row in rs:       
        w={'rid':row[0],'name':row[1],'phno':row[3],'amail':row[4],'location':row[5],'phid':row[8]}
        list.append(w)
    return render(request,'bookart.html',{'list':list})

def bookartact(request):
    artid=request.GET['rid']
    bdate=request.GET['bdate']
    rem=request.GET['rem']
    cursor=connection.cursor()
    s="insert into tbl_booking(artid,uid,bkdate,descp,status) values('%s','%s','%s','%s','pending')" %(artid,request.session['uid'],bdate,rem)
    cursor.execute(s)
    msg="<script>alert('Artist Booking Request Send');window.location='/vimg/';</script>"
    return HttpResponse(msg)

def mybooking(request):
    cursor=connection.cursor()
    s="SELECT * FROM tbl_cusreg,tbl_booking where tbl_cusreg.rid=tbl_booking.artid and tbl_booking.uid = '%s'"%(request.session['uid'])
    cursor.execute(s)
    rs=cursor.fetchall()
    list=[]
    for row in rs:       
        w={'bkid':row[8],'name':row[1],'phno':row[3],'amail':row[4],'location':row[5],'bkdate':row[11],'descp':row[12],'status':row[13]}
        list.append(w)
    return render(request,'mybooking.html',{'list':list})


def bookingreq(request):
    cursor=connection.cursor()
    s="SELECT * FROM tbl_cusreg,tbl_booking where tbl_cusreg.rid=tbl_booking.uid and tbl_booking.artid = '%s'"%(request.session['uid'])
    cursor.execute(s)
    rs=cursor.fetchall()
    list=[]
    for row in rs:       
        w={'bkid':row[8],'name':row[1],'phno':row[3],'amail':row[4],'location':row[5],'bkdate':row[11],'descp':row[12],'status':row[13]}
        list.append(w)
    return render(request,'bookingreq.html',{'list':list})

def bkaccept(request):
    bkid=request.GET['bkid']
    cursor=connection.cursor()
    s="update tbl_booking set status='accepted' where bkid = %s" %(bkid)
    cursor.execute(s)
    msg="<script>alert('Request Accepted');window.location='/bookingreq/';</script>"
    return HttpResponse(msg)

def bkreject(request):
    bkid=request.GET['bkid']
    cursor=connection.cursor()
    s="update tbl_booking set status='rejected' where bkid = %s" %(bkid)
    cursor.execute(s)
    msg="<script>alert('Request Rejected');window.location='/bookingreq/';</script>"
    return HttpResponse(msg)

def bkupdate(request):
    cursor=connection.cursor()
    bkid=request.GET['bkid']
    s="SELECT * FROM tbl_cusreg,tbl_booking where  tbl_booking.bkid = '%s' and tbl_cusreg.rid=tbl_booking.artid"%(bkid)
    cursor.execute(s)
    rs=cursor.fetchall()
    list=[]
    for row in rs:       
        w={'bkid':row[8],'name':row[1],'phno':row[3],'amail':row[4],'location':row[5],'status':row[13],'rem':row[12]}
        list.append(w)
    return render(request,'bookart1.html',{'list':list})

def bkupdateact(request):
    bkid=request.GET['bkid']
    rem=request.GET['rem']
    bdate=request.GET['bdate']
    cursor=connection.cursor()
    s="update tbl_booking set bkdate='%s',descp='%s'where bkid = %s" %(bdate,rem,bkid)
    cursor.execute(s)
    msg="<script>alert('Booking Details Updated');window.location='/mybooking/';</script>"
    return HttpResponse(msg)

def bkdelete(request):
    bkid=request.GET['bkid']
    cursor=connection.cursor()
    s="delete from tbl_booking where bkid = %s" %(bkid)
    cursor.execute(s)
    msg="<script>alert('Request Rejected');window.location='/mybooking/';</script>"
    return HttpResponse(msg)

def vbiding(request):
    cursor=connection.cursor()
    ad=request.GET['ad']
    s="SELECT * FROM tbl_biding,tbl_cusreg WHERE tbl_biding.uid = tbl_cusreg.rid and tbl_biding.aucid=%s ORDER BY bidamt DESC,bidtime ASC "%(request.GET['aid'])
    cursor.execute(s)
    rs=cursor.fetchall()
    list=[]
    for row in rs:       
        w={'bidid':row[0],'aid':row[1],'uname':row[8],'btime':row[5],'bamt':row[2],'status':row[6],'phon':row[10]}
        list.append(w)
    #if request.session['utype']=='admin':
    s1="SELECT bidid,bidate FROM tbl_biding,tbl_cusreg WHERE tbl_biding.uid = tbl_cusreg.rid and tbl_biding.aucid=%s ORDER BY bidamt DESC,bidtime ASC limit 1"%(request.GET['aid'])
    cursor.execute(s1)
    rs1=cursor.fetchall()
    bidid=0    
    bdate=""    
    for row1 in rs1:       
        bidid=row1[0]
        bdate=row1[1]
    return render(request,'vbiding.html',{'list':list,'bidid':bidid,'ad':ad,'bdate':str(bdate),'cd':datetime.datetime.today().strftime("%Y-%m-%d")})
    ''' elif request.session['utype']=='artist':
        return render(request,'vresult1.html',{'list':list})
    elif request.session['utype']=='user':
        return render(request,'vresult2.html',{'list':list})'''

def bidupdate(request):
    bid=request.GET['bidid']
    cursor=connection.cursor()
    s="update tbl_biding set status ='sold' where bidid = %s" %(bid)
    cursor.execute(s)

    s="select aucid from tbl_biding where bidid = %s" %(bid)
    cursor.execute(s)
    rs1=cursor.fetchall()
    aid=0        
    for row1 in rs1:       
        aid=row1[0]

    s="update tbl_biding set status ='sold out' where aucid = %s and bidid <> %s" %(aid,bid)
    cursor.execute(s)

    s="update tbl_auction set status ='sold' where aucid = %s " %(aid)
    cursor.execute(s)

    msg="<script>alert('Auction status Updated');window.location='/myauction/';</script>"
    return HttpResponse(msg)

def delbid(request):
    bid=request.GET['bid']
    cursor=connection.cursor()
    s="delete from tbl_biding where bidid = %s" %(bid)
    cursor.execute(s)
    msg="<script>alert('Request Rejected');window.location='/myauction/';</script>"
    return HttpResponse(msg)