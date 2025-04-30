# if, elif, else
# allows different pathways for our code to take, on certain conditions being met.

#is_verified = False
#is_admin = True
#'on_holiday = False

#if (is_admin or is_verified) and not on_holiday:
#    print("access granted")
#else:
#    print("no access")

#import dis

#def example():
#    x = 0
#    while x < 3:
#        x += 1

#dis.dis(example)

# if elif else

#temp = 23

#if temp >= 30:
#    print("its very hot")
#elif temp > 25:
#    print("still quite warm")
#elif temp > 10:
#    print("it ok")
#else:
#    print("not good")


# multiple comparators

#deposit = 100
#password = "password2"

#if 0 <  deposit < 100 and password == "password":
#    print("deposit ok")
#else:
#    print("no allowed")

# not

#if not 0 < deposit < 100 and password != "password":
#    print("not allowed")
#else:
#    print("thanks")


# in and not in

#name = "root"

#if name in ("root", "admin", "password"):
#    print("invalid")
#else:
#    print("accpeted")

#if name not in ("root", "admin", "password"):
#    print("accepted")
#else:
#    print("denied")

# exercise:

# weight converter app
# user to input weight
# user to input kgs or lbs
# logic: check unit input
# logic: convert to corresponding unit. (kgs - lbs)
# print out value. 
# error handling: unit input (loops/upper/lower)
# optional: error handling for non-numeric input in weight.  


#BaseException 

#Exception(BaseException)

#ZeroDivisionError(Exception)

#try:
#    result = 10/0
#except ZeroDivisionError: # consumes the error
#    print("Division by zero is not allowed")
#except Exception as e:
#    print(f"[ERROR] - an error occured - {str(e)}")
#except: # Same as Baaseexception
#    pass
#finally:
#    print("Clean up actions")
#    db.close()

# solution:
#import sys

#while True:
#    try:
 #       weight = float(input("enter a weight: "))
#        break
#    except ValueError:
#        print("invalid input - must be numerical!!")
 #       sys.exit()

#while True:
#    unit = input("Enter K (kgs) or L (lbs): ").upper()
 #   if unit == "K":
 #       converted = weight / 0.45
 #       print(f"weight in lbs is {converted}")
  #      break
   # elif unit == "L":
   #     converted = weight * 0.45
   #     print(f"weight in kgs is {converted}")
   #     break
   # else:
   #     print("invalid choice!! K or L please")