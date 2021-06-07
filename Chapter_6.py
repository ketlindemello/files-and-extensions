
def validate_input(message):
    while True:
        user_input = str(input(message))
        if user_input.isspace() == False and len (user_input) != 0:
            return user_input

        else:
            print('You must provide requested information!')

user_name = validate_input('Enter your name: ')
user_description = validate_input('Enter a sentence that describes yourself: ')

try:
    file = open('person.html','w')

    html_format = '''<html>

    <head>
    <title> ''' + user_name + ''' </title>

    </head>

    <body>

    <center>

    <h1 style='background-color:powderblue; color:blue; font-size:300%;'>''' + user_name + '''</h1>
    <hr/>  <p style = color:red; font-family:courier;'>''' + user_description + ''' </p> <hr/>

    </center>
    
    </body>

    </html>'''

    file.write(html_format)
    file.close()
    

except IOError:
    print('An error ocurred trying to create the file', person.html)


print(user_name + ' Your personalized web page was created!')



