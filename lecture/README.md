# 윈도우에서 파이썬 설치 및 개발환경 설정하기
---

## 파이썬을 이용해 프로그램을 개발하자

---

[##_Image|kage@l8AGo/btrIMB3uBQO/9l9Q1MeoWJOrXaBiarcrA0/img.jpg|CDM|1.3|{"originWidth":507,"originHeight":146,"style":"alignCenter","width":null}_##]

  
파이썬은 전세계에서 다섯 손가락 안에 꼽히는 인기 프로그래밍 언어입니다. 기존에 프로그래밍을 배우지 않은 분들이 쉽게 이용할 수 있는 형식과, 자연어에 약간(아주 약간이지만) 가까운 문법 때문인가봅니다. 그리고 다른 프로그래밍 언어와 달리, 프로그램 개발 속도가 아주 빠르고 심지어는 완성시키지 않고도 이용할 수 있기도 합니다.  
  

[##_Image|kage@HJPOP/btrIEY0rOmI/tfCTtvjgkWBzj3EFAGEQbK/img.png|CDM|1.3|{"originWidth":256,"originHeight":256,"style":"alignCenter","width":null}_##]

  
저는 개발자가 되기 전에 디자이너를 위한 프로그래밍 언어라고 불리는 액션스크립트를 이용했었습니다. 그 때는 전문적인 프로그램이나 분석보다 게임을 만들고 싶었으니 나름 좋은 선택이었지요. 하지만 본격적으로 개발자가 될 결심을 하고는 파이썬을 배웠습니다. 애초에 프로그래밍에 대한 전문적인 교육을 받지 않았으니 입문이 쉬운 언어가 우선이었지요.  
  
어쨌든, 이렇게 프로그래밍 전공이 아닌 사람이 가르쳐주는 파이썬 이야기입니다.

---

## 파이썬 설치

---

[##_Image|kage@cnQcpU/btrIJVhmjfE/13tyOZ90uH6VnUj7OGktQK/img.jpg|CDM|1.3|{"originWidth":1237,"originHeight":560,"style":"alignCenter","width":null}_##]

  
파이썬 설치는 [파이썬 공식 홈페이지](http://python.org)로 접속해 시작합니다. 영어가 막 적혀있지만, 다운로드(Doenload)라는 말은 알아보기 쉽죠. 위에 있는 메뉴에서 Downloads 버튼을 누른 뒤 알맞은 버전을 다운로드합시다.  
  
파이썬은 크게 2.7버전과 3.X버전을 이용하는 추세인데, 2버전과 3버전의 호환이 되지 않는 코드가 있기 때문에 이용하려는 기능에 따라 선택하거나, 가상환경을 만들어 둘 다 사용하는 방법이 있습니다. 옛날 패키지나 자연과학 분야라면 2.7버전이 필요한 경우가 있으나, 2.7버전을 굳이 이용해야 할 상황이 아니라면 최신 버전을 다운로드해도 문제 없습니다.  
  
파이썬 설치는 설치 프로그램을 실행해 지시대로 하면 되며, 처음 설치시에는 **Add Python (버전) to PATH** 항목을 체크해주는게 사용하기 편리합니다.

---

## 파이썬 실행

---

파이썬 설치 후에는 프로그래밍 개발환경을 구축한 뒤 으레 하는 **"Hello, World!"**를 출력할 차례입니다. 시작 버튼을 누른 뒤 IDLE을 치고 엔터를 누르면 파이썬의 기본 개발환경인 IDLE Shell을 만나볼 수 있습니다.  
  

[##_Image|kage@d0GMxS/btrIKmZ4ETC/BmngdLPdx0lebE8EVMCZE0/img.jpg|CDM|1.3|{"originWidth":591,"originHeight":596,"style":"alignCenter","width":null}_##]

  
IDLE Shell은 명령어를 하나 치고 엔터를 누르면 그 결과가 바로 뜨는 인터프리터입니다. 대충 코드 몇 줄을 실행하거나 공부하는 입장에는 좋지만, 전문적인 개발을 위해서는 다른 IDE(통합개발환경)을 준비하는 것이 좋지요. 이 부분은 다음에 안내드리겠습니다.  
  
여기에

```
print("Hello, Wolrd!")
```

위 코드를 입력한다면 아래와 같이 출력이 나옵니다.

[##_Image|kage@oIUG2/btrIKmThUOS/ZaV9mnLQkmgsCqJidPHkQ1/img.jpg|CDM|1.3|{"originWidth":591,"originHeight":187,"style":"alignCenter","width":null}_##]

  
  
이렇게 기본적인 코드 실행 방법을 알아내면 이제 간단한 코드를 실행해서 프로그래밍에 대한 기본적인 감각을 느껴보는게 차례입니다.