import random

y = 0

while(y < 3):
	
	y = int(input("\n'0: 가위, 1: 바위, 2: 보' 중에서 하나를 선택하세요\n(다른 숫자를 누르면 종료합니): "));

	x = random.randint(0, 3)
	if(x == 0):
		computer = "가위";
	elif(x == 1):
		computer = "바위";
	else:
		computer = "보";
	
	if(y == 0):
		player = "가위";
	elif(y == 1):
		player = "바위";
	elif(y == 2):
		player = "보";
	else:
		break
	
	print("\n사용자: ",player,"컴퓨터: ",computer)
		
	if(player == computer):
		print("비겼음!");
	elif(player == "바위"):
		if(computer == "보"):
			print("컴퓨터가 이겼음!");
		else:
			print("사용자가 이겼음!");
	elif(player == "보"):
		if(computer == "가위"):
			print("컴퓨터가 이겼음!");
		else:
			print("사용자가 이겼음!");
	elif(player == "가위"):
		if(computer == "바위"):
			print("컴퓨터가 이겼음!");
		else:
			print("사용자가 이겼음!");

	continue

print("\n게임 종료")
