# Task_1: Explore in Google and Make a document :

# 1. Why we use conditions:
'''Why We Use Conditions: Conditions allow us to control what the program does and perform different actions based on these “if, then” logic statements. 
   What makes computer programs great is the ability to interact with a user- this is only possible with conditions that direct this type of interaction.'''

# 2. Difference between if and elif?
'''Difference between if and if elif else
Python will evaluate all three if statements to determine if they are true. 
Once a condition in the if elif else statement is true, Python stop evaluating the other conditions. 
Because of this, if elif else is faster than three if statements.'''

# 3. What is difference between operator and variable?
'''to write statements using variables, which store values like numbers and words, and operators, which are symbols that perform a computation. 
    We also explain three kinds of programming errors and offer additional debugging advice.'''

# 4. What is indentation? how many tab spaces it will take?
'''Indenting text adds structure to your document by allowing you to separate information. 
    Whether you'd like to move a single line or an entire paragraph, 
    you can use the tab selector and the horizontal ruler to set tabs and indents.
    In terms of how many spaces (or tabs) constitutes indentation, it's more important to be consistent throughout your code than to use any specific tab stop value.'''
    
# 5. How to write if block (syntax)?
'''The IF statement is similar to that of other languages. 
The if statement contains a logical expression using which the data is compared and a decision is made based on the 
result of the comparison.
     -----Syntax-----
        if expression:
        statement(s)'''


# Task_2:

# Write a program,  my age is more than 20 print teen_age other wise print younge_age?
# 	a.my_age is 20, who am i? Expected output: you are teen_age
# 	b.my_age is 30, who am i? Expected output: you are younge_age
# 	c.my_age is 10, who am i? 
# 	d.my_age is 40, who am i? 
def age(age):
    if age >20:
        print("you are teen_age")
    else:
        print("you are younge_age")

age(10)

# Write a program today is Monday/Tuesday/Wendsday/Thursday/Friday print weekday otherwise print weekend?
def dayss(days):
    if days == "Monday" or days == "Tuesday" or days == "Wendsday" or days == "Thursday" or days == "Friday":
        print("weekday")
    else:
        print("weekend")
dayss("sunday")
    

# Task_3: 

# Scenario1: Today my business income is 10/- if my income is more than 10/- then print "i am profitable" otherwise print "i lost"
# ఈ రోజు నా ఆదాయం 10. నా ఆదాయం 10 కంటే ఎక్కువ ఉంటే ప్రింట్ నేను లాభదాయకంగా ఉన్నాను లేకపోతే నేను పోగొట్టుకున్నాను.
def income(income):
    if income >10:
        print("i am profitable")
    else:
        print("i lost")
income(9)

# Scenario2: your age is more than your sister age then print "i am elder" otherwise print "i am younger"
# మీ వయస్సు మీ సోదరి వయస్సు కంటే ఎక్కువగా ఉంటే, నేను పెద్దవాడిని అని ముద్రించండి లేకపోతే నేను చిన్నవాడిని అని ముద్రించండి
my_age=10
sis_age=8
def my_agee(my_age,sis_age):
    if my_age > sis_age:
        print("i am elder")
    else:
        print("i am younger")
my_agee(my_age,sis_age)


# Scenario3:festival offer in my shop. 
# purchase amount more than 100 then print 30% discount.
#  purchase amount less than 50 then print 10% discount 
#  otherwise print 20% discount.
#  నా దుకాణంలో పండుగ ఆఫర్. కొనుగోలు మొత్తం 100 కంటే ఎక్కువ, ఆపై ప్రింట్ 30% తగ్గింపు. 50 కంటే తక్కువ మొత్తాన్ని కొనుగోలు చేసి, ఆపై 10% తగ్గింపును ప్రింట్ చేయండి లేకపోతే 20% తగ్గింపును ప్రింట్ చేయండి
#  मेरी दुकान में त्योहार की पेशकश। खरीद राशि 100 से अधिक तो 30% छूट प्रिंट करें। खरीद राशि 50 से कम है तो 10% छूट प्रिंट करें अन्यथा 20% छूट प्रिंट करें।
def offer(amount):
    if amount >100:
        off=amount*.30
        print(off) 
    elif amount <50:
        off=amount*.10
        print(off)
    else:
        off=amount*.20
        print(off)
offer(40) 
 
#  Scenario4:my movie theater prices. price is 140 print balcony. price is 50 print chair. price is 100 print bench 
# నా సినిమా థియేటర్ ధరలు. ధర 140 ప్రింట్ బాల్కనీ. ధర 50 ప్రింట్ కుర్చీ. ధర 100 ప్రింట్ బెంచ్
def movie_theater(price):
    if price == 140:
        print("Balcony")
    elif price == 50:
        print("Chair")
    elif price == 100:
        print("Bench")
    else:
        ("Not Available")
movie_theater(140)

# Scenario5: my showroom vehicle types. 
# if vehicle type is two wheeler print bike and scooty. 
# if vehicle type is four wheeler print car, loory, van and zeep
# నా షోరూమ్ వాహనాల రకాలు. వాహనం రకం టూ వీలర్ ప్రింట్ బైక్ మరియు స్కూటీ అయితే. వాహనం రకం ఫోర్ వీలర్ ప్రింట్ కారు అయితే, లూరీ, వ్యాన్ మరియు జీప్

def showroom_vehicle(vehicle_type):
    if vehicle_type == "two wheeler":
        print("bike and scooty")
    elif vehicle_type == "four wheeler":
        print("car, loory, van and zeep")
    else:
        print("wrong input")
showroom_vehicle("four wheeler")

