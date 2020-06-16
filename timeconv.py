s = str(input("Enter time in 12-hr format AM or PM : "))
hh=s[0:2]
mm=s[3:5]
ss=s[6:8]
ff=s[8:10]
if(1<=int(hh)<=12 and 00<=int(mm)<=59 and 00<=int(ss)<=59):
    if (ff == "AM"):
        if(hh =="12"):
            HH ="00"
        else:
            HH = hh
    elif(ff == "PM"):
       if (hh== "12"):
           HH=hh
       else:
           HH=str(int(hh)+12)
    else:
        print("Time format error!")
else:
    print("Time format error!")
print("Time in 24-hr : "+ HH+":"+mm+":"+ss)

