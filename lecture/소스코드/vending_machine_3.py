itemName = '커피'
itemPrice = 300

bill = int(input("1000원 지폐개수: "))
coin500 = int(input("500원 동전개수: "))
coin100 = int(input("100원 동전개수: "))
total = bill * 1000 + coin500 * 500 + coin100 * 100

for i in range(0, 3): # i가 1~3까지 증가하며 반복된다.

  buyCoffee = int(input("%s 몇 잔을 구매할까요?: " % itemName))

  if (total - buyCoffee * itemPrice) >= 0:
    total = total - buyCoffee * itemPrice
    print("%s %d잔을 구매했습니다." %(itemName, buyCoffee))
  else:
    print("돈이 부족합니다. 남은 금액은 반환합니다.")
    break # 돈이 부족할 경우, 반복문을 빠져나온다.

nCoin500 = total // 500
total = total % 500

nCoin100 = total // 100

print("반환된 500원: %d 개\n반환된 100원: %d 개" % (nCoin500, nCoin100))
