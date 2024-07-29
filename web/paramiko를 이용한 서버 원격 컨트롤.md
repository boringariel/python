## 파이썬 paramiko를 이용한 서버 원격 컨트롤
---
서버 관리를 하거나 다른 컴퓨터에 원격으로 접속을 할 때는 SSH를 이용해 명령어를 전송하는 방식을 주로 사용합니다. GUI가 편한 분들이라면 팀뷰어나 애니데스크 등의 원격 조작 프로그램을 이용할 수도 있지만, 사양이나 네트워크 상태 등의 변수로 인해 속도가 현저하게 느려질 수도 있고, CLI만 지원하는 프로그램을 위해 GUI 원격 접속을 하는건 낭비이기도 하죠.
</p></br></br>

파이썬(Python)을 이용한 개발 또는 자동화 작업에서도 원격 조작이 필요할 때가 있습니다. 기본적인 파일 관리나 명령은 파이썬 내부에서 수행할 수 있지만, 다른 컴퓨터에 명령을 내리는건 별개의 이야기입니다. 그래서 파이썬으로 원격 명령을 내리는 파라미코(paramiko)라는 패키지를 소개해 드리겠습니다.
</p></br></br>

### paramiko 설치하기
---
paramiko는 SSH 접속을 통해 서버를 원격 조작할 수 있는 패키지입니다. 쉽게 말해, 우리가 putty 등의 프로그램을 이용해 다른 서버에 접속하는 일을 파이썬 내부에서 할 수 있게 해 주는 패키지입니다. paramiko 설치는 pip 패키지 관리자를 이용해 쉽게 할 수 있답니다.
</p></br></br>

```bash
$pip install paramiko
```
</p></br></br>

### paramiko 이용하기
---
paramiko를 이용한 간단한 서버 원격 컨트롤 예제를 살펴보도록 하겠습니다. 이번 예제에서는 IP 주소가 192.168.0.123 인 서버에 SSH 접속을 하는 상황을 가정해 보겠습니다. 이 때, user 라는 사용자가 password 라는 비밀번호를 사용하고 있다면, 아래와 같이 접속 코드를 작성할 수 있습니다.
</p></br></br>

```python
# import package
import paramiko

# server info.
server = '192.168.0.123'
user = 'user'
pwd = 'password'
port = 22

# connect
cli = paramiko.SSHClient()
cli.set_missing_host_key_policy(paramiko.AutoAddPolicy)
cli.connect(ip, port=port, username=user, password=pwd)

# print hello
stdin, stdout, stderr = cli.exec_command('echo "Hello!"')
output = stdout.read().decode('utf8')

print(output)
```
</p></br></br>

위 코드를 입력하게 된다면, 파이썬 콘솔에 Hello! 가 출력되게 됩니다. 이 출력문은 로컬에서 실행된게 아니라, 192.168.0.123 서버에서 출력된 Hello! 문자열을 다운로드해서 로컬에 출력한 코드입니다.
</p></br></br>

### 함수 설명
---
위 코드에서, `cli.set_missing_host_key_policy(paramiko.AutoAddPolicy)` 부분은 호스트 키 없이 서버에 연결할 때 자동으로 연결하는 정책입니다. 다른 설정을 원한다면 `paramiko.AutoAddPolicy` 부분을 알맞은 정책으로 변경하시면 됩니다.
</p></br></br>

`cli.connect(ip, port=port, username=user, password=pwd)` 부분은, CLI 명령을 보낼 수 있도록 SSH 연결을 하는 함수입니다. IP, 포트, 사용자이름, 비밀번호 순서로 매개변수를 입력받지요. IP는 해당 서버나 라우터에서 확인할 수 있으며, 포트는 기본적으로 22를 사용하지만 서버 설정에 따라 다른 포트를 이용해야 할 수 있으니, 미리 서버 관리자에게 확인해 주세요.
</p></br></br>

`stdin, stdout, stderr = cli.exec_command('echo "Hello!"')` 부분이 접속한 서버에 명령어를 전달하는 함수입니다. 해당 서버의 운영체제에 따라 알맞은 명령어를 매개변수로 입력해 주면 됩니다. 저는 리눅스 운영체제를 가정하고 `'echo "Hello!"'` 를 입력했습니다. 'Hello!'를 출력하는 명령어죠. 이 코드를 실행하면, 반환값이 input, output, error message 순서로 반환됩니다. 그래서 이 메시지들은 각각 stdin, stdout, stderr 순서로 할당되는거죠.
</p></br></br>

stdin, stdout, stderr는 일반적으로 print() 함수를 통해 내용물을 볼 수 없습니다. 그래서 해당 변수를 UTF-8 인코딩된 문자열로 변환하기 위해 `output = stdout.read().decode('utf8')` 명령어를 입력해 줍니다. 여기서 stdout 대신 stdin이나 stderr를 변환할 경우, 입력한 명령어 또는 에러 로그를 문자열로 확인할 수 있게 되지요. 참고로, read() 함수는 리턴값을 한 줄씩 읽을 수 있는 함수이므로 여러 줄이 나오는 출력의 경우, read()를 반복하는 식으로 이용할 수 있습니다.
</p></br></br>

만약, 여러 줄로 출력되는 리턴값을 한번에 읽어들이고 싶다면 `read()` 함수를 반복하는 대신 `readlines()` 라는 대안을 사용할 수 있습니다. 이 함수는, 반환값의 여러 줄을 리스트 형식으로 분리해 리턴하며, 이 결과물은 문자열 형식으로 반환하기 때문에 `decode()` 함수를 추가할 필요가 없다는 장점도 있답니다.
