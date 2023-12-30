months = ['January', 'February', 'March']
total_sales = [52000.00, 51000.00, 48000.00]
production_cost = [46800.00, 45900.00, 43200.00]

for month, total, cost in zip(months, total_sales, production_cost):
    print('Общая прибыль в', month, '=', total - cost)