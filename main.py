min_price = 1.0

# cписок покупок
purchases = [
    {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
    {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
    {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
]

# item — название товара
# category — категория товара
# price — цена за единицу товара
# quantity — количество единиц, купленных за один раз

def total_revenue(purchases):
    # функция, которая рассчитывает и возвращает общую выручку (цена * количество для всех записей)
    revenue = 0

    for purchase in purchases:
        revenue += purchase["price"] * purchase["quantity"]
    
    return revenue

def items_by_category(purchases):
    # функция, которая возвращает словарь, где ключ — категория, а значение — список уникальных товаров в этой категории
    category_dict = dict()
    items_list = list()

    for purchase in purchases:
        category_dict.setdefault(purchase["category"])

    for item in category_dict:
        for purchase in purchases:
            if purchase["category"] == item:
                items_list.append(purchase["item"])
        category_dict[item] = items_list
        items_list = list()

    return category_dict

def expensive_purchases(purchases, min_price):
    # функция, которая выводит все покупки, где цена товара больше или равна min_price
    purchases_list = list()

    for purchase in purchases:
        if purchase["price"] >= min_price:
            purchases_list.append(purchase)

    return purchases_list

def average_price_by_category(purchases):
    # функция, которая рассчитывает среднюю цену товаров по каждой категории
    average_dict = dict()
    price_list = list()

    for purchase in purchases:
            average_dict.setdefault(purchase["category"])

    for item in average_dict:
        for purchase in purchases:
            if purchase["category"] == item:
                price_list.append(purchase["price"])
        average_dict[item] = sum(price_list) / (len(price_list))
        price_list = list()

    return average_dict

def most_frequent_category(purchases):
    # функция, которая находит и возвращает категорию, в которой куплено больше всего единиц товаров (учитывая поле quantity)
    category_dict = dict()
    max_quantity_category = str()
    category_quantity = 0
    max_quantity = 0

    for purchase in purchases:
        category_dict.setdefault(purchase["category"])

    for item in category_dict:
        for purchase in purchases:
            if purchase["category"] == item:
                category_quantity += purchase["quantity"]
        if category_quantity > max_quantity:
            max_quantity = category_quantity
            max_quantity_category = item
        category_quantity = 0

    return max_quantity_category

print(f"Общая выручка: {total_revenue(purchases)}")
print(f"Товары по категориям: {items_by_category(purchases)}")
print(f"Покупки дороже {min_price}: {expensive_purchases(purchases, min_price)}")
print(f"Средняя цена по категориям: {average_price_by_category(purchases)}")
print(f"Категория с наибольшим количеством проданных товаров: {most_frequent_category(purchases)}")