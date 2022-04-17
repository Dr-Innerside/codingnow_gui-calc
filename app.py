import tkinter as tk

disValue = 0                                                                            # 초기값을 0으로 변수 초기화

def number_click(value):
    print('숫자',value)
    global disValue
    disValue = (disValue*10) + value
    str_value.set(disValue)

def operator_click(value):
    print('명령', value)
def button_click(value):
    # print(value)

    # 숫자와 오퍼레이터를 나누기 위한
    try:
        value = int(value)
        number_click(value)
    except:
        operator_click(value)



win = tk.Tk()
win.title('계산기')

str_value = tk.StringVar()                                                              # 문자열로 표시
str_value.set(str(disValue))                                                            # 초깃값을 문자열로 변환
dis = tk.Entry(win, textvariable=str_value, justify="right", bg='white', fg='red')        # 에디터 엔트리 형식에 넣기
dis.grid(column=0, row=0, columnspan= 4, ipadx=80, ipady=30)                            # 에디터 위치, 크기 조정

# 버튼을 반복문 형태로 만들기
# 버튼에 들어갈 배열 선언
calItem = [['1','2','3','4'],
           ['5','6','7','8'],
           ['9','0','+','-'],
           ['/','*','C','=']]
# 버튼을 만들어줄 반복문 선언
# calItem의 인덱스(리스트의 번호)가 i에, 리스트 내용이 item에 들어감
for i,items in enumerate(calItem):
    # 네 개로 묶인 item을 각각 인덱스(k)와 하나의 버튼 값(item)으로 들어감
    for k, item in enumerate(items):
        # 초기에 만든 버튼에서 들어갈 버튼의 이름(text)에 item 값이,
        # 열에 해당하는 값이 k가 되고, 행에 해당하는 값이 에디터보다 밑에 들어와야 해서 i+1값

        # 특정 부분만 색깔넣기
        try:
            # 버튼 값을 정수로 변환
            # 정수로 변환했을 때 연산자는 오류가 나는 것을 이용
            color = int(item)
            color = 'black'
        except:
            color = 'green'


        bt = tk.Button(win,
                       text=item,
                       width=10,
                       height=5,
                       bg=color,
                       fg='white',
                       # 간이 함수 생성, cmd에 item 값을 넣고 버튼클릭 함수에 인자를 넣어 실행
                       command=lambda cmd=item: button_click(cmd))

        bt.grid(column=k, row=(i+1))


# tk.Button(win, text='1', width=10, height=5).grid(column=0, row=1)
# tk.Button(win, text='2', width=10, height=5).grid(column=1, row=1)
# tk.Button(win, text='3', width=10, height=5).grid(column=2, row=1)
# tk.Button(win, text='4', width=10, height=5).grid(column=3, row=1)
#
# tk.Button(win, text='5', width=10, height=5).grid(column=0, row=2)
# tk.Button(win, text='6', width=10, height=5).grid(column=1, row=2)
# tk.Button(win, text='7', width=10, height=5).grid(column=2, row=2)
# tk.Button(win, text='8', width=10, height=5).grid(column=3, row=2)
#
# tk.Button(win, text='9', width=10, height=5).grid(column=0, row=3)
# tk.Button(win, text='0', width=10, height=5).grid(column=1, row=3)
# tk.Button(win, text='+', width=10, height=5).grid(column=2, row=3)
# tk.Button(win, text='-', width=10, height=5).grid(column=3, row=3)
#
# tk.Button(win, text='/', width=10, height=5).grid(column=0, row=4)
# tk.Button(win, text='*', width=10, height=5).grid(column=1, row=4)
# tk.Button(win, text='C', width=10, height=5).grid(column=2, row=4)
# tk.Button(win, text='=', width=10, height=5).grid(column=3, row=4)



win.mainloop()