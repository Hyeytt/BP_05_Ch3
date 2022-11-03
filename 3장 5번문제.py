import turtle                     # turtle 함수 불러오기

t = turtle.Turtle()               # t값을 turtle 함수로 변환

t.shape("turtle")                 # t 모양을 거북이 모양으로 설정

t.left(45)                        # 왼쪽으로 45도 회전

t.fd(141)                         # 앞으로 141만큼 이동

t.setheading(0)                   # 거북이 머리를 0도로 설정

t.goto(0, 0)                       # 0,0 으로 이동

t.fd(100)                         # 앞으로 100만큼 이동

t.left(90)                        # 왼쪽으로 90도 회전

t.fd(100)                         # 앞으로 100만큼 이동

t. _screen.exitonclick()          # 클릭하여 화면 종료
