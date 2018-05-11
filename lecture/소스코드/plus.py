x = 0
y = 0

for i in range(1, 101):
  y += i
  x = i
  if(y > 100):
      break

print("정수 값 "+str(x)+"까지의 합은 "+str(y)+"입니다.")
