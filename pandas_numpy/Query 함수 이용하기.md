![readme_1](./image/readme_1.jpg)

## 판다스 Query 함수 이용하기

---

파이썬에서 판다스 (Pandas) 를 이용할 때 특정 조건에 맞는 데이터를 추출하고 싶을 때가 있습니다. 그럴 때는 일반적으로 마스킹 (masking) 을 사용하지만, 복잡한 조건이나 외부 함수를 참조하는 상황, 여러가지 조건 적용 등의 활용에서는 불편함이 있습니다.

이럴때는 Query (쿼리) 함수를 사용해 간단하게 해결할 수 있습니다. Query 함수는 대소 비교나 부분검색, 외부 함수 참조 등의 다양한 기능을 지원합니다.

Query 함수는 pandas.DataFrame.query(expr) 형식으로 이용합니다. 특이한 점으로는 조건문 (expr) 에 해당하는 항목을 문자열로 작성한다는 부분이 있겠네요.

---

## Query 함수로 마스킹하기

---

Query 함수를 이용하는 법을 간단한 마스킹을 통해 알아보도록 합시다.

```
import pandas as pd
data = {'A': [1,2,3,3,3], 'B': ['hello','world','python','pandas','query']}
df = pd.DataFrame(data)
print(df)
```

우선은 위 코드를 입력해 예제에 사용할 데이터프레임을 만들어줍니다. A, B는 각 column 이름이며, [1,2,3,3,3], ['hello','world','python','pandas','query']가 각각 A, B의 value로 할당됩니다.

이 때, A column의 value가 3인 데이터만 보고 싶을 때, Query 함수를 어떻게 사용하는지 알아보죠.

```
query_expr = 'A == 3'
df2 = df.query(query_expr)
print(df2)
```

이렇게 조건문을 설정하면 A가 3인 항목들만 출력됩니다. 조건문이 query_expr라는 변수에 문자열로 저장되어 있기 때문에, 특정 상황에서 조건이 변동되는 프로그램을 만들 때 Query 함수가 유용하게 사용될 수 있습니다.

---

## Query 함수 활용하기

---

Query 함수는 상기한 조건 이외에도, 다양한 조건을 이용할 수 있습니다. 가령 A column에서 사용할 경우에는

A == b	A와 b가 일치하는 항목
A != b	A와 b가 일치하지 않는 항목
A > b	A가 b보다 큰 항목
A < b	A가 b보다 작은 항목
A >= b	A가 b 이상인 항목
A <= b	A가 b 이하인 항목


이러한 활용을 할 수 있지요. column 이름 대신 index를 사용하고 싶다면, 간단하게 index라고 적으면 됩니다. Query 함수는 또한 외부 함수를 이용할 수도 있습니다. 문자열 안에 조건을 입력하는 Query의 특성상, 함수를 이용할 때 @를 이용해 구분해야 합니다.

```
def num2():
    return 2

query_expr = 'A == @num2'
df2 = df.query(query_expr)
print(df2)
```

위와 같은 코드를 입력할 경우, A가 2에 해당하는 데이터만 볼 수 있게 됩니다.

또한, Query 함수의 조건문에는 변수를 입력할 수도 있습니다. 변수를 입력하는 방법은 함수와 마찬가지로 @ 표기를 할 수도 있고, f-string이라는 방법을 이용해 표기할 수도 있습니다. f-string을 이용하는 방법은 아래 코드와 같습니다.

```
msg = 'hel'
msg += 'lo'

query_expr = f'B == {msg}'
df2 = df.query(query_expr)
print(df2)
```

위와 같이, Query 함수에 변수를 이용하는 경우 같은 구문으로도 조건을 다르게 설정할 수 있어 유용하게 활용할 수 있습니다.