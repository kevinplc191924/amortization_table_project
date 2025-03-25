from amortization_table import LoanAmortization
import matplotlib.pyplot as plt

loan = LoanAmortization(loan_amount=5000, annual_rate=0.1275, periods_per_year=2, years=5)
table = loan.get_table()
print(table)

amort_total = table['Amortization'].sum()
print('The sum of the amortization column is: ${:.2f}'.format(amort_total))

# Plotting interest against amortization
fig, ax = plt.subplots(figsize=(10, 4))
fig.suptitle('Interest vs Amortization')

ax.plot(table.index, table['Interest'], color='blue')
ax.set_ylabel('Interest', color='blue')
ax.tick_params('y', colors='blue')
ax.set_xlabel('Periods')

ax_second = ax.twinx()
ax_second.plot(table.index, table['Amortization'], color='red')
ax_second.set_ylabel('Amortization', color='red')
ax_second.tick_params('y', colors='red')

plt.show()