units=int(input("Enter number of electricity units:"))
bill=units*8
if units>=0 and units<=50:
    bill=0
elif units>=51 and units<=100:
    bill=bill*5
elif units<101:
    bill=bill*8
elif units>=300:
    bill=bill+500
else:
    bill=bill+100
gst=bill*18/100
total_bill=bill+gst
print("Electricy bill",bill)
print("gst =",gst)
print("Total_bill",total_bill)