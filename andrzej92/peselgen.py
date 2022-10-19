#!/usr/bin/env python3

from datetime import date, timedelta

def pos_to_checksum_multiplier(pos):
    match pos % 4:
        case 0:
            return 1
        case 1:
            return 3
        case 2:
            return 7
        case 3:
            return 9

def pesel_checksum(pesel):
    partial = 0
    pos = 0
    for d in pesel:
        partial += int(d) * pos_to_checksum_multiplier(pos)
        pos += 1

    return partial % 10

def verify(pesel):
    return (pesel_checksum(pesel[:-1]) + int(pesel[-1])) % 10 == 0

def pesel_gen(birth_date, serial):
    year = birth_date.year % 100
    month = birth_date.month
    if birth_date.year >= 2000:
        month += 20
    day = birth_date.day

    partial_pesel = f'{year:02}{month:02}{day:02}{serial:04}'
    partial_chksum = pesel_checksum(partial_pesel)

    return partial_pesel + str((-partial_chksum) % 10)

def main():
    male = True
    birth_date = date(year=1992, month=12, day=22)
    day = timedelta(days=1)

    while True:
        for serial in range(0, 9999, 2):
            if male:
                serial += 1
            for card_ending in range(10000):
                print(pesel_gen(birth_date, serial) + f'{card_ending:04}')
        birth_date += day

if __name__ == '__main__':
    main()

