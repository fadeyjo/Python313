import re

numbers = ['+7 499 456-45-78', '+74994564578', '7 (499) 456 45 78', '7 (499) 456-45-78']

pattern = r'[+]?7\s?[(]?\d{3}[)]?\s?\d{3}(?:\s|-)?\d{2}(?:-|\s)?\d{2}'

print('Корректные номера телефонов:', re.findall(pattern, ' '.join(numbers)))