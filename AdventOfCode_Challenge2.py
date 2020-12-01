expense_report = []
entries = None

inputFile = open('.\\input.txt', 'r')
for expense in inputFile:
    expense_report.append(int(expense.rstrip('\n')))

inputFile.close()


for x in range(len(expense_report)): # Add third loop and check all 3 numbers
    for y in range(x + 1, len(expense_report)):
        if (expense_report[x] + expense_report[y] >= 2020):
            continue
        for z in range(x + 2, len(expense_report)):
            if (expense_report[x] + expense_report[y] + expense_report[z] == 2020):
                entries = (expense_report[x], expense_report[y], expense_report[z])
                break
        if (entries is not None):
            break
    if (entries is not None):
        break


print(entries)
print(entries[0] * entries[1] * entries[2])
