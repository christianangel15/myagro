def get_days_of_power(R1, D1, R2, D2, R3, D3, K):

    LoanDayAmnt = {
        D1: R1,
        D2: R2,
        D3: R3
    }
    days = []
    rate = []
    for key in sorted(LoanDayAmnt):
        days.append(key)
        rate.append(LoanDayAmnt[key])
    # print('Day and rate created')
    index = -1
    Power = 0
    while True:
        if (K < rate[0]) or (K < (rate[0] + rate[1])) or (K < (rate[0]+rate[1]+rate[2])):
            break
        index += 1
        # print(f'Day {index} started')
        if (index >= days[0]) and (index < days[1]):
            K -= rate[0]
            # print(f'{K}-1')
            Power += 1
        elif (index >= days[1]) and (index < days[2]):
            K -= (rate[0]+rate[1])
            # print(f'{K}-2')
            Power += 1
        elif (index >= days[2]):
            K -= (rate[0]+rate[1]+rate[2])
            # print(f'{K}-3')
            Power += 1
    return (f'Total Days of Power = {Power} days')


print(get_days_of_power(1000, 3, 500, 10, 1500, 7, 21000))
