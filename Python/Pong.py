#!/usr/bin/python2.7
import simpleguitk
import math

def key_handler(key):
	global o, t
	#paddle controls w,s and up,down arrows
	if (int(key) == 83):
		o += 30
	if (int(key) == 87):
		o -= 30
	if (int(key) == 40):
		t += 30
	if (int(key) == 38):
		t -= 30

def reset():
	global o, t, x, y, changeX, changeY
	o = 250
	t = 250
	x = 300
	y = 300
	changeX = 4
	changeY = 0
	
def draw_handler(canvas):
	global o, t, x, y, changeX, changeY, playerOne, playerTwo
	#Scoreboard
	canvas.draw_text("Score:", (495, 25), 12, 'Red')
	canvas.draw_text(playerOne, (500, 40), 12, 'Red')
	canvas.draw_text(":", (512, 40), 12, 'Red')
	canvas.draw_text(playerTwo, (520, 40), 12, 'Red')
	#paddles
	canvas.draw_line((10,o),(10,o+100), 5 ,"White")
	canvas.draw_line((590,t),(590,t+100), 5 ,"White")
	#ball
	canvas.draw_circle((x, y), 10, 1, "White", "White")
	x += changeX
	y += changeY
	
	#Check for point loss
	if (x <= 0):
		playerTwo += 1
		reset()
	elif (x >= 600):
		playerOne += 1
		reset()
			
	#changing ball velocity
	if((x >= 580) and ((y >= t) and (y <= t+100))):
		#paddle 1
		relativeIntersectY = (t+(100.0/2.0)) - y
		
		normalizedRelativeIntersectionY = (relativeIntersectY/(100.0/2.0))
		bounceAngle = normalizedRelativeIntersectionY * (5*3.14/12)
		
		changeX = 4*-math.cos(bounceAngle)
		changeY = 4*-math.sin(bounceAngle)
	elif((x <= 20) and ((y >= o) and (y <= o+100))):
		#paddle 2
		relativeIntersectY = (o+(100.0/2.0)) - y
		
		normalizedRelativeIntersectionY = (relativeIntersectY/(100.0/2.0))
		bounceAngle = normalizedRelativeIntersectionY * (5*3.14/12)
		
		changeX = 4*math.cos(bounceAngle)
		changeY = 4*-math.sin(bounceAngle)
		
	#Check if hitting top or bottom wall
	elif(y >= 580):
		changeY = -changeY

	elif(y <= 20):
		changeY = -changeY



o = 250
t = 250
x = 300
y = 300
changeX = 4
changeY = 0
playerOne = 0
playerTwo = 0
frame = simpleguitk.create_frame('Testing', 600, 600)
frame.set_keydown_handler(key_handler)
frame.set_canvas_background("Black")
frame.set_draw_handler(draw_handler)
frame.start()