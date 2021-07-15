import random
import matplotlib.pyplot as plt

roles = 1000000

dict = {
    1:0,
    2:0,
    3:0,
    4:0,
    5:0,
    6:0
}

for i in range(roles):
    dict[random.randint(1,6)] += 1

print([key for key in dict],[Pair for Pair in dict.values()])

plt.pie([Pair for Pair in dict.values()], labels=[key for key in dict], autopct='%1.1f%%', shadow=True, startangle=90)
plt.show()

