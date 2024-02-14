import time

start = time.time()

PRICE_OF_BULL = 10
PRICE_OF_COW = 5
PRICE_OF_CALF = 0.5

for quantity_of_bulls in range(101):
    for quantity_of_cows in range(101):
        for quantity_of_calfs in range(0, 101, 2):
            if quantity_of_bulls + quantity_of_cows + quantity_of_calfs == quantity_of_bulls * PRICE_OF_BULL + quantity_of_cows * PRICE_OF_COW + quantity_of_calfs * PRICE_OF_CALF == 100:
                print(f'Количество быков: {quantity_of_bulls}.')
                print(f'Количество коров: {quantity_of_cows}.')
                print(f'Количество телёнков: {quantity_of_calfs}.')

end = time.time()

print(f'Время выполнения программы: {end - start}')