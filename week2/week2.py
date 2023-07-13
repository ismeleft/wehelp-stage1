print("==== 第一題：====")


def find_and_print(messages):
    over_17 = []
    # 判斷是否大於17歲的準則，是否說出自己的年紀（包含成年）、是否已上大學、是否具有投票權
    for neme, message in messages.items():
        if "18 years old" in message or "college student" in message or "legal age" in message or "vote" in message:
            over_17.append(neme)

    for name in over_17:
        print(name)


find_and_print({
    "Bob": "My name is Bob. I'm 18 years old.",
    "Mary": "Hello, glad to meet you.",
    "Copper": "I'm a college student. Nice to meet you.",
    "Leslie": "I am of legal age in Taiwan.",
    "Vivian": "I will vote for Donald Trump next week",
    "Jenny": "Good morning."
})


print("==== 第二題：====")


def calculate_sum_of_bonus(data):

    # 根據薪水跟表現、職位來計算獎金，並要求獎金總合不能超過台幣10000
    # 故獎金發放規則為表現平均0.07個月薪，表現低於平均0.03個月薪，表現高於平均0.1個月薪，職位獎金CEO為bonus＊1.2
    # 將薪水計算成台幣，利用匯率為30
    # 將薪水（字串轉為數字）
    # 利用if判斷式將表現狀況與月薪、職位做換算為獎金
    # 逐一印出獎金後相加
    exchange_rate = 30
    total_bonus = 0

    for employee in data["employees"]:
        name = employee["name"]
        salary = employee["salary"]
        performance = employee["performance"]
        role = employee["role"]

        if isinstance(salary, str):
            if "USD" in salary:
                salary = int(salary.replace("USD", "")) * exchange_rate
            else:
                salary = int(salary.replace(",", ""))

        if performance == "above average":
            bonus = salary * 0.1
        elif performance == "average":
            bonus = salary * 0.07
        else:
            bonus = salary * 0.03

        if role == "Engineer":
            bonus *= 1
        elif role == "CEO":
            bonus *= 1.2
        else:
            bonus *= 1

        total_bonus += bonus
    print(total_bonus)


calculate_sum_of_bonus({
    "employees": [
        {
            "name": "John",
            "salary": "1000USD",
            "performance": "above average",
            "role": "Engineer"
        },
        {
            "name": "Bob",
            "salary": 60000,
            "performance": "average",
            "role": "CEO"},
        {
            "name": "Jenny",
            "salary": "50,000",
            "performance": "below average",
            "role": "Sales"
        }]
})


print("==== 第三題：====")


def func(*data):
    middle_names = {}
    unique_name = None

    for name in data:
        middle_name = name[1]
        if middle_name in middle_names:
            middle_names[middle_name] = None
        else:
            middle_names[middle_name] = name

    for name in data:
        middle_name = name[1]

        if middle_names.get(middle_name) == name:
            unique_name = name

    if unique_name:
        print(unique_name)
    else:
        print("沒有")


func("彭大牆", "王明雅", "吳明")
func("郭靜雅", "王立強", "林靜宜", "郭立恆", "林花花")
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花")


print("==== 第四題：====")


def get_number(index):
    # 由觀察可知，奇數引數跟偶數引數皆遞增3，偶數引數從0開始遞增3，奇數引數也會等於後一個引數+1
    if index == 0:
        return 0
    if index % 2 == 0:
        return get_number(index-2)+3
    if index % 2 == 1:
        return get_number(index+1)+1


print(get_number(1))
print(get_number(5))
print(get_number(10))
