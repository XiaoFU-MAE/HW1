#ECON435 HW1 Q2(b)
#Author: Xiao FU
#UID:305448673

import lxml.etree
doc = lxml.etree.parse("FoodServiceData.xml")
count = doc.xpath('count(//TypeDescription)')
count1=0
count2=0
count3=0
count4=0
count5=0
count6=0
count7=0
count8=0
count9=0
count10=0
count11=0
count12=0
count13=0
count14=0
count15=0
count16=0
count17=0
count18=0
count19=0
for item in doc.findall('foodservice/TypeDescription'):
    if item.text == 'CATERERS':
        count1+=1

    elif item.text == 'FOOD SERVICE':
        count2+=1
    elif item.text == 'FOOD SERVICE (DAY CARE / CHILD CARE CENTER':
        count3+=1
    elif item.text == 'FOOD SERVICE (HOSPITAL / NURSING HOME':
        count4+=1
    elif item.text == 'FOOD SERVICE COMMISSARY':
        count5+=1
        
    elif item.text == 'HOME (CONTINENTAL BREAKFAST)':
        count6+=1
    elif item.text == 'HOME (FULL BREAKFAST)':
        count7+=1
    elif item.text == 'INN (FULL BREAKFAST)':
        count8+=1
    elif item.text == 'MOBILE RESTRICTED CONCESSION':
        count9+=1
    elif item.text == 'PRE-PACKAGED RETAIL':
        count10+=1
    elif item.text == 'RETAIL BAKERY':
        count11+=1
    elif item.text == 'RETAIL WITH LIMITED SERVICE':
        count12+=1
    elif item.text == 'RETAIL-FOOD  10,000 SQ FT OR LESS':
        count13+=1
    elif item.text == 'RETAIL-FOOD  10,001 SQ FT OR OVER':
        count14+=1
    elif item.text == 'SALVAGE DISTRIBUTOR':
        count15+=1
    elif item.text == 'SCHOOL CAFETERIA OR FOOD SERVICE':
        count16+=1
    elif item.text == 'SELF-CONTAINED MOBILE FOOD UNITS':
        count17+=1
    elif item.text == 'STATIONARY RESTRICTED CONCESSON':
        count18+=1
    elif item.text == 'SUPERMARKET WITH PROCESSING':
        count19+=1
    
    
        
print('CATERERS',count1)
print('FOOD SERVICE',count2)
print('FOOD SERVICE (DAY CARE / CHILD CARE CENTER',count3)
print('FOOD SERVICE (HOSPITAL / NURSING HOME',count4)
print('FOOD SERVICE COMMISSARY',count5)

print('HOME (CONTINENTAL BREAKFAST)',count6)
print('HOME (FULL BREAKFAST)',count7)
print('INN (FULL BREAKFAST)',count8)
print('MOBILE RESTRICTED CONCESSION',count9)
print('PRE-PACKAGED RETAIL',count10)
print('RETAIL BAKERY',count11)
print('RETAIL WITH LIMITED SERVICE',count12)
print('RETAIL-FOOD  10,000 SQ FT OR LESS',count13)
print('RETAIL-FOOD  10,001 SQ FT OR OVER',count14)
print('SALVAGE DISTRIBUTOR',count15)
print('SCHOOL CAFETERIA OR FOOD SERVICE',count16)
print('SELF-CONTAINED MOBILE FOOD UNITS',count17)
print('STATIONARY RESTRICTED CONCESSON',count18)
print('SUPERMARKET WITH PROCESSING',count19)


#Q2(c)
import lxml.etree
doc = lxml.etree.parse("FoodServiceData.xml")
countA=0
countB=0
countC=0
countNA=0

for item in doc.findall('foodservice/Grade'):
    if item.text == 'A':
        countA+=1

    elif item.text == 'B':
        countB+=1
    elif item.text == 'C':
        countC+=1
    else:
        countNA+=1
    
    
print('A',countA)
print('B',countB)
print('C',countC)
print('No grade',countNA)


