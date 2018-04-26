itemName = '커피'
itemPrice = 300

bill = int(input("1000원 지폐개수: "))
coin500 = int(input("500원 동전개수: "))
coin100 = int(input("100원 동전개수: "))
total = bill * 1000 + coin500 * 500 + coin100 * 100

buyCoffee = int(input("%s 몇 잔을 구매할까요?: " % itemName))

#+ 이 부분이 수정된 알고리즘에 해당하는 코드이다.
if (total - buyCoffee * itemPrice) >= 0:
  total = total - buyCoffee * itemPrice
  print("%s %d잔을 구매했습니다." %(itemName, buyCoffee))
else:
  print("돈이 부족합니다. 남은 금액은 반환합니다.")
#-

nCoin500 = total // 500
total = total % 500

nCoin100 = total // 100

print("반환된 500원: %d 개\n반환된 100원: %d 개" % (nCoin500, nCoin100))
