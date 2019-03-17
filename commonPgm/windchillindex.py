v=input("enter the wind speed:")
t=input("enter the temp:")
if v>=0 and v<=4:
    print"wind chillindex WCI=",t
elif v>=5 and v<=44:
    print "wind chillindex WCI=",91.4+(91.4-t)*(0.00203*v-0.304*v*.5-0.474)
elif v>=45:
    print"wind chillindex WCI=",1.6*t-55