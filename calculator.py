# Imports
from tkinter import *

# Global variables
expression = ''
expressionPart = ''
operationPressed = False
gotResult = False

# Helper functions
def check_error():
    global expression, expressionPart, gotResult

    if label['text'] == 'Error':
        expression = ''
        expressionPart = ''
        label['text'] = '0'
        gotResult = False

def check_zero_division():
    global expression, expressionPart
    if expressionPart != '':
        if '/0' in expressionPart[-2:] or '/0.' in expressionPart[-3:]:
            label['text'] = 'Error'
            expressionPart = ''
            expression = ''
            clearButton['text'] = 'AC'
        elif expressionPart[-1] == '/' and (label['text'] == '0' or label['text'] == '0,'):
            label['text'] = 'Error'
            expressionPart = ''
            expression = ''
            clearButton['text'] = 'AC'
        return 0

def check_last_character(someExpression):
    if someExpression[-1] in ',+-/*':
        someExpression = someExpression[:-1]
    return someExpression

def round_result(someExpression):
    if someExpression != '':
        if (eval(someExpression) % 1 == 0 or eval(someExpression) == 0) and len(str(eval(someExpression))) < 10:
            someExpression = str(int(eval(someExpression)))
            label['text'] = someExpression.replace('.', ',')
        else:
            if len(str(eval(someExpression))) < 10 and 'e' not in str(eval(someExpression)):
                someExpression = str((eval(someExpression)))
                label['text'] = someExpression.replace('.', ',')
            elif len(str(int(eval(someExpression)))) >= 10 or 'e' in str(eval(someExpression)):
                someExpression = "%10.3e" % (eval(someExpression))
                label['text'] = someExpression.replace('.', ',')
            else:
                someExpression = str((eval(someExpression)))[:11]
                label['text'] = someExpression.replace('.', ',')
            someExpression = label['text'].replace(',', '.')
    return someExpression

def set_default_button_colors():
    additionButton['background'] = orange
    subtractionButton['background'] = orange
    multiplicationButton['background'] = orange
    divisionButton['background'] = orange

    additionButton['foreground'] = white
    subtractionButton['foreground'] = white
    multiplicationButton['foreground'] = white
    divisionButton['foreground'] = white

# Functions for the calculations
def add_number_to_expression(someExpression):
    global expression
    if label['text'] != 'Error':
        someExpression += label['text'].replace(',', '.')
    return someExpression

def add_number_to_label(number):
    global expression, operationPressed, gotResult

    if operationPressed:
        label['text'] = ''
        set_default_button_colors()
        operationPressed = False

    if gotResult:
        label['text'] = ''
        set_default_button_colors()
        expression = ''
        gotResult = False

    check_error()
    if label['text'] == '0':
        label['text'] = str(number)
    elif label['text'] == '-0':
        label['text'] = '-' + str(number)
    else:
        label['text'] += str(number)

    clearButton['text'] = 'C'

def add_comma():
    global expression, operationPressed, gotResult

    if operationPressed:
        label['text'] = '0'
        set_default_button_colors()
        operationPressed = False

    if gotResult:
        label['text'] = ''
        set_default_button_colors()
        expression = ''
        gotResult = False

    check_error()
    if ',' not in label['text']:
        label['text'] += ','

    clearButton['text'] = 'C'
    print(expression)

def clear():
    global expression, gotResult, operationPressed

    if clearButton['text'] == 'AC':
        expression = ''
    elif clearButton['text'] == 'C':
        clearButton['text'] = 'AC'
    label['text'] = '0'

    set_default_button_colors()
    operationPressed = False
    gotResult = False
    print(expression)

def addition():
    global expression, operationPressed, expressionPart, gotResult

    check_error()
    set_default_button_colors()

    if not gotResult and not operationPressed:
        expression = add_number_to_expression(expression)
        check_zero_division()

    if expressionPart != '':
        expression += expressionPart
        expressionPart = ''

    if expression != '':
        expression = check_last_character(expression)

    expression = round_result(expression)
    expression += '+'
    gotResult = False
    operationPressed = True

    additionButton['background'], additionButton['foreground'] = additionButton['foreground'], additionButton['background']
    print(expression)

def subtraction():
    global expression, operationPressed, expressionPart, gotResult

    check_error()
    set_default_button_colors()

    if not gotResult and not operationPressed:
        expression = add_number_to_expression(expression)
        check_zero_division()

    if expressionPart != '':
        expression += expressionPart
        expressionPart = ''

    if expression != '':
        expression = check_last_character(expression)

    expression = round_result(expression)
    expression += '-'
    gotResult = False
    operationPressed = True

    subtractionButton['background'], subtractionButton['foreground'] = subtractionButton['foreground'], subtractionButton['background']
    print(expression)

def multiplication():
    global expression, operationPressed, expressionPart, gotResult

    check_error()
    set_default_button_colors()

    if not gotResult and not operationPressed:
        expressionPart = add_number_to_expression(expressionPart)
        check_zero_division()

    if expressionPart != '':
        expressionPart = check_last_character(expressionPart)
    elif expression != '':
        expression = check_last_character(expression)

    expressionPart += '*'
    gotResult = False
    operationPressed = True

    multiplicationButton['background'], multiplicationButton['foreground'] = multiplicationButton['foreground'], multiplicationButton['background']
    print(expressionPart)
    print(expression)

def division():
    global expression, operationPressed, expressionPart, gotResult

    check_error()
    set_default_button_colors()

    if not gotResult and not operationPressed:
        expressionPart = add_number_to_expression(expressionPart)
        check_zero_division()

    if expressionPart != '':
        expressionPart = check_last_character(expressionPart)
    elif expression != '':
        expression = check_last_character(expression)

    expressionPart += '/'
    gotResult = False
    operationPressed = True

    divisionButton['background'], divisionButton['foreground'] = divisionButton['foreground'], divisionButton['background']
    print(expressionPart)
    print(expression)

def plus_minus():
    global expression, operationPressed, expressionPart

    check_error()

    if operationPressed:
        label['text'] = '0'
        operationPressed = False

    if label['text'][0] == '-':
        label['text'] = label['text'][1:]
    elif operationPressed:
        label['text'] = '-0'
        operationPressed = False
    else:
        label['text'] = '-' + label['text']
    print(expression)

# def percent():
#     global expression, operationPressed
#
#     print(expression)

def equals():
    global expression, expressionPart, gotResult

    if not gotResult and expressionPart == '':
        expression = add_number_to_expression(expression)
        expression = check_last_character(expression)
    elif expressionPart != '':
        expressionPart = add_number_to_expression(expressionPart)
        expression += expressionPart
    print(expression)
    check_zero_division()
    expression = round_result(expression)
    expressionPart = ''
    clearButton['text'] = 'AC'
    gotResult = True
    print(expression)


# Colors for the GUI
black = '#000000'
white = '#ffffff'
darkgray = '#333333'
lightgray = '#a5a5a5'
orange = '#f28b01'
borderColor = '#2a2a2a'
red = '#ff0000'

# Setting up the window
windowWidth = 450
windowHeight = 630

window = Tk()
window.overrideredirect(True)
window.geometry(f'{windowWidth}x{windowHeight}')
window['background'] = black
window.resizable(0, 0)

# Creating the border
borderHeight = 30

border = Canvas(window, highlightthickness=0)
border.create_rectangle(0, 0, windowWidth - 2, borderHeight, fill=borderColor)

buttonBorder = 4
exitButton = Button(
    border, text='x', name='exitButton', background=red, foreground=black, border=0, font=('Helvetica', 10),
    command=lambda: window.destroy()
)
exitButton.place(x=410, y=0 + buttonBorder, width=40 - buttonBorder, height=borderHeight - 2 * buttonBorder)

# Hiding the border
hiddenBorder = Canvas(window, highlightthickness=0)
hiddenBorder.place(x=1, y=1, width=windowWidth - 2, height=borderHeight)
hiddenBorder.create_rectangle(0, 0, windowWidth - 2, borderHeight, fill=black)

def hide_border():
    border.place(x=0, y=0, width=0, height=0)
    hiddenBorder.place(x=1, y=1, width=windowWidth - 2, height=borderHeight)

def reveal_border():
    border.place(x=1, y=1, width=windowWidth - 2, height=borderHeight)
    hiddenBorder.place(x=0, y=0, width=0, height=0)


hiddenBorder.bind('<Enter>', lambda event: reveal_border())
border.bind('<Leave>', lambda event: hide_border())

# Moving the window
mouseX = None
mouseY = None

def move_window(event):
    global mouseX, mouseY
    deltaX = event.x - mouseX
    deltaY = event.y - mouseY
    newX = window.winfo_x() + deltaX
    newY = window.winfo_y() + deltaY

    window.geometry(f'+{newX}+{newY}')

def on_press(event):
    global mouseX, mouseY
    mouseX = event.x
    mouseY = event.y

def on_release():
    global mouseX, mouseY
    mouseX = None
    mouseY = None


border.bind('<ButtonPress-1>', on_press)
border.bind('<ButtonRelease-1>', lambda event: on_release())
border.bind('<B1-Motion>', move_window)

# Creating the buttons
buttonWidth = windowWidth / 5
buttonHeight = (windowHeight - borderHeight) / 8
spaceInBetween = windowWidth / 5 / 5

numberButtons = []
for row in range(3):
    for column in range(3):
        buttonNumber = 3*row+column+1
        numberButtons.append(Button(
            window, text=f'{buttonNumber}', name=f'button{buttonNumber}', background=darkgray, foreground=white,
            border=0,  font=('Helvetica', 25), command=lambda number=buttonNumber: add_number_to_label(number))
        )
        numberButtons[-1].place(
            x=(column + 1) * spaceInBetween + column * buttonWidth,
            y=windowHeight - (3 + row) * spaceInBetween - (2 + row) * buttonHeight, width=buttonWidth,
            height=buttonHeight
        )
numberButtons.append(Button(
    window, text='0', name='0', background=darkgray, foreground=white, border=0, font=('Helvetica', 25),
    command=lambda number=0: add_number_to_label(number)
))
numberButtons[-1].place(
    x=spaceInBetween, y=windowHeight - 2*spaceInBetween - buttonHeight, width=2*buttonWidth+spaceInBetween,
    height=buttonHeight
)

commaButton = Button(
    window, text=',', name='comma', background=darkgray, foreground=white, border=0, font=('Helvetica', 25),
    command=add_comma
)
commaButton.place(
    x=3*spaceInBetween+2*buttonWidth, y=windowHeight-2*spaceInBetween-buttonHeight, width=buttonWidth,
    height=buttonHeight
)

clearButton = Button(
    window, text='AC', name='clear', background=lightgray, foreground=black, border=0, font=('Helvetica', 25),
    command=clear
)
clearButton.place(
    x=spaceInBetween, y=windowHeight-6*spaceInBetween-5*buttonHeight, width=buttonWidth,
    height=buttonHeight
)

plusMinusButton = Button(
    window, text='+/-', name='plusminus', background=lightgray, foreground=black, border=0, font=('Helvetica', 25),
    command=plus_minus
)
plusMinusButton.place(
    x=2*spaceInBetween+buttonWidth, y=windowHeight-6*spaceInBetween-5*buttonHeight, width=buttonWidth,
    height=buttonHeight
)

# percentButton = Button(
#     window, text='%', name='percent', background=lightgray, foreground=black, border=0, font=('Helvetica', 25),
#     command=percent
# )
# percentButton.place(
#     x=3*spaceInBetween+2*buttonWidth, y=windowHeight-6*spaceInBetween-5*buttonHeight, width=buttonWidth,
#     height=buttonHeight
# )

divisionButton = Button(
    window, text='/', name='division', background=orange, foreground=white, border=0, font=('Helvetica', 25),
    command=division
)
divisionButton.place(
    x=4*spaceInBetween+3*buttonWidth, y=windowHeight-6*spaceInBetween-5*buttonHeight, width=buttonWidth,
    height=buttonHeight
)

multiplicationButton = Button(
    window, text='x', name='multiplication', background=orange, foreground=white, border=0, font=('Helvetica', 25),
    command=multiplication
)
multiplicationButton.place(
    x=4*spaceInBetween+3*buttonWidth, y=windowHeight-5*spaceInBetween-4*buttonHeight, width=buttonWidth,
    height=buttonHeight
)

subtractionButton = Button(
    window, text='-', name='subtraction', background=orange, foreground=white, border=0, font=('Helvetica', 25),
    command=subtraction
)
subtractionButton.place(
    x=4*spaceInBetween+3*buttonWidth, y=windowHeight-4*spaceInBetween-3*buttonHeight, width=buttonWidth,
    height=buttonHeight
)

additionButton = Button(
    window, text='+', name='addition', background=orange, foreground=white, border=0, font=('Helvetica', 25),
    command=addition
)
additionButton.place(
    x=4*spaceInBetween+3*buttonWidth, y=windowHeight-3*spaceInBetween-2*buttonHeight, width=buttonWidth,
    height=buttonHeight
)

equalsButton = Button(
    window, text='=', name='equals', background=orange, foreground=white, border=0, font=('Helvetica', 25),
    command=equals
)
equalsButton.place(
    x=4*spaceInBetween+3*buttonWidth, y=windowHeight-2*spaceInBetween-1*buttonHeight, width=buttonWidth,
    height=buttonHeight
)

# Label for the calculation
label = Label(
    window, text='0', name='expression', background=black, foreground=white, font=('Helvetica', 50), anchor='e'
)
label.place(
    x=spaceInBetween, y=windowHeight-7*spaceInBetween-6*buttonHeight, width=windowWidth-2*spaceInBetween-5,
    height=buttonHeight
)

# Controlling with keyboard
window.bind('0', lambda event: add_number_to_label(0))
window.bind('1', lambda event: add_number_to_label(1))
window.bind('2', lambda event: add_number_to_label(2))
window.bind('3', lambda event: add_number_to_label(3))
window.bind('4', lambda event: add_number_to_label(4))
window.bind('5', lambda event: add_number_to_label(5))
window.bind('6', lambda event: add_number_to_label(6))
window.bind('7', lambda event: add_number_to_label(7))
window.bind('8', lambda event: add_number_to_label(8))
window.bind('9', lambda event: add_number_to_label(9))
window.bind('<comma>', lambda event: add_comma())

window.bind('<Return>', lambda event: equals())
window.bind('<slash>', lambda event: division())
window.bind('<asterisk>', lambda event: multiplication())
window.bind('<minus>', lambda event: subtraction())
window.bind('<plus>', lambda event: addition())
window.bind('<Up>', lambda event: plus_minus())
window.bind('<Down>', lambda event: plus_minus())
window.bind('<Delete>', lambda event: clear())

# Running the application
window.mainloop()
