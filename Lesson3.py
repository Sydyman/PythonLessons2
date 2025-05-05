x = 26
y = 19

if type(x) == int and type(y) == int:
    print(x + y)

list2 = [12,12,12,13,13,45,67]

def buble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] =arr[j + 1],arr[j]
    return arr

sortNums = buble_sort(list2)
print(sortNums)

day = input("кто ты ? \n")

match day:
    case "я":
        print("головка ты ")
    case " а ты ":
        print("я это ты а ты это я")








