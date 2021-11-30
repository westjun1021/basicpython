print("\n"*45)



def add_item(item, amount, t_inventory):
    if check_item(item, t_inventory):
         t_inventory[item] += amount
         print(item+"의 수량이"+str( t_inventory[item])+"개 입니다.")
    else:
        t_inventory[item]=amount
        print(item+"이 추가되었습니다.")

def remove_item(item, t_inventory):
    if check_item(item, t_inventory):
        t_inventory[item]=0
        print(item+"의 수량이 0이 되었습니다.")
    else:
        print(item+"이 존재하지 않습니다.")

def consume_item(item, t_inventory):
    if check_item(item, t_inventory):
        if t_inventory[item]<=0:
            print("현재 아이템 수량이 적어서 사용할수 없습니다.")
        else:
            t_inventory[item]-=1
            print(item+"의 수량은"+str(t_inventory[item])+"입니다.")
    else:
        print(item+"이 존재하지 않습니다.")

def check_item(item, t_inventory):
    return item in t_inventory

def print_itemMenu():
    print("0. 끝내기")
    print("1. 아이템 추가")
    print("2. 아이템 삭제")
    print("3. 아이템 확인")
    print("4. 아이템 사용")

    
def use_item(inventory):
    while True:
        print_itemMenu()
        option=int(input("메뉴 번호를 입력하세요."))
        if option ==0:
            print("종료합니다")
            break
        elif option == 1:
            new_item=input("아이템을 입력하세요.)")
            amount=int(input("수량을 입력하세요.)"))
            add_item(new_item, amount, inventory)       
        elif option == 2:
            eliminated_item=input("아이템을 입력하세요.)")
            remove_item(eliminated_item, inventory)       
        elif option == 3:
            print(inventory)
            
        elif option == 4:
            c_item=input("사용할 아이템을 입력하세요.")
            consume_item(c_item, inventory)
        
        else:
            print("잘못된 번호를 입력하셨습니다.")
        



character={}
select_character=None
def new_character(name, t_character):
    if  check_character(name, t_character):
        print("이미 존재하는 이름입니다.")
    else:
        inventory = {}
        t_character[name]=inventory
        
        
def check_character(name, t_character):
    return name in t_character

def print_characterMenu():
    print("0. 끝내기")
    print("1. 캐릭터 추가")
    print("2.캐릭터 이름출력")
    print("3. 캐릭터 선택")
    print("4. 캐릭터 인벤토리 조작")
    
while True:
    print_characterMenu()
    option=int(input("메뉴를 선택해주세요.)"))
    if option==0:
        print("종료되었습니다.")
        break
    
    elif option==1:
        name=input("캐릭터 이름을 입력하세요")
        new_character(name, character)
        
    elif option==2:
        i=1
        print("###############")
        for name in character.keys():
            print(str(i)+","+name)
            i+=1
        print("###############")
        
    elif option==3:
        temp_name=input("선택할 캐릭터의 이름을 입력해주세요.")
        if check_character(temp_name, character):
            select_character=temp_name
            print(select_character+"이 선택되었습니다.")
        else:
            print(temp_name+"이(는) 존재하지 않는 캐릭터입니다.")

    elif option==4:
        if select_character ==None:
            print("3번 메뉴로 캐릭터를 선택해주세요.")
        else:
            print("선택된 캐릭터는"+select_character+"입니다.")
            inventory=character[select_character]
            use_item(inventory)
            
            
        








