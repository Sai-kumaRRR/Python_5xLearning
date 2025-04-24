Products = {
    {"name": "laptop", "price": 100},
    {"name": "smart phone", "price": 1000},
    {"name": "table", "price": 300},
    {"name": "Heap phone", "price": 100},
}
print(type(Products)),
print(type(Products[0]))


def is_affortable(sai):
    return items["price"] < 500



items = list(filter(is_affortable, Products))

for i in is_affortable:
    print(i["price"], i["name"])

    i = 10
    name = "sai"
    print(i)
    print(name)
    print(name + str(i))
    print(int(name) + i)
