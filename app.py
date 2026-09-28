print ("hello world")
#data type
student_count=100;# int
rating =98.6; # float
subject= "python"#char
print(student_count)
print(rating)
print(subject)
##SyntaxWarning
print ("python program will start")
course = "python program for beginner"
print(len(course))# len of the string
print(course[0])# index of the string
print(course[0:])
print(course[0:5])
print(course[:])
print(course[-5])
#escape
subject='python\n program'
print (subject)
#concatned
first="anusha"
second="shetty"
full = first + " " +second
print(full)
#\n
course ="  python programing"
print(course.upper())
print(course.lower())
print(course.title())
print(course.rstrip())
print(course.find("pro"))
print(course.replace("p","k"))
print ("pro" in course)
print("swift" in course)
#type number
x=10
x=12.9
x= 3+3j
print(3+5)
print(5-2)
print(9*4)
print(4%7)
print(3/7)
print(4//8)
print(4**5)
#increament number
x=10
x =x+9
x+=9
#decreament number
x=5
x=x-4
x-=7
print(round(3.7))
print(abs(8.8))
print(abs(-9.5))
x= input ("x:")
y= int(x)+1
print(f"x: {x},y:{y}")