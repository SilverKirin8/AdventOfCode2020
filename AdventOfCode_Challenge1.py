expense_report = []
entries = None

inputFile = open('.\\input.txt', 'r')
for expense in inputFile:
    expense_report.append(int(expense.rstrip('\n')))

inputFile.close()


for x in range(len(expense_report)):
    for y in range(x + 1, len(expense_report) - 1):
        if (expense_report[x] + expense_report[y] == 2020):
            entries = (expense_report[x], expense_report[y])
            print(x)
            print(y)
            break
    if (entries is not None):
        break


print(entries)
print(entries[0] * entries[1])