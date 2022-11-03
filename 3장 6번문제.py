import turtle                       # turtle 함수 불러오기

t = turtle.Turtle()                 # t값을 turtle 함수로 변환

t.shape("turtle")                   # t 모양을 거북이 모양으로 설정

x1 = int(input("x1 : "))

y1 = int(input("y1 : "))

x2 = int(input("x2 : "))

y2 = int(input("y2 : "))

dist = ((x1 - x2) ** 2 + (y1 - y2)**2) ** 0.5      # **를 사용하여 거듭제곱

t.up()  # 펜 들어올리기

t.goto(x1, y1)

t.down()  # 펜 내리기

t.goto(x2, y2)

t.write("점의 길이 = " + str(dist))   # 문자열 간의 조합이기 때문에 '+' 사용

t. _screen.exitonclick()              # 클릭하여 사라지게 하기
