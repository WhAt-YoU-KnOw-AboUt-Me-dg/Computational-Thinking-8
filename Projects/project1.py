###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################
q1 = codesters.Square(100, 100, 200, 'blue')
q2 = codesters.Square(-100, 100, 200, 'purple')
q3 = codesters.Square(-100, -100, 200, 'teal')
q4 = codesters.Square(100, -100, 200, 'black')
s1 = codesters.Sprite("unname", 100, 100)
s1.set_size (0.5)
s2 = codesters.Sprite("hip-hop", -100, -100)
s2.set_size (0.05)
s3 = codesters.Sprite("disco", -100, 100)
s3.set_size (0.5)
s4 = codesters.Sprite("taps", 100, -100)
s4.set_size (0.5)