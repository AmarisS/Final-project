import random
import numpy as np
import pandas as pd
import datetime
import calendar
import sys
import matplotlib.pyplot as plt

class CheckQueue():
    def __init__(self):
        """
        create an empty queue
        """
        self.items = []

    def enqueue(self, item):
        """
        add new passenger to the end of queue
        :param item: reference
        :return: null
        """
        self.items.insert(0, item)

    def dequeue(self):
        """
        remove the passenger at the beginning of the queue
        :return: null
        """
        item = self.items.pop()
        return item

    def isEmpty(self):
        """
        check if there is passengers in the current waiting queue
        :return: boolean value
        """
        return 0 == len(self.items)

    def number_of_items(self):
        """
        return the number of items in the queue
        :return
        """
        length = len(self.items)
        return length


def math_automatictime(l, u):
    """
    calculate the automatic machine check time for passengers with carry-on luggage
    k: the number of security check entrance
    rho: = l/u, the efficiency of one security check entrance. When rho>1, the line grows. Else, the line decreases.
    :param l: the assumed number of passengers that arrive the security check entrance in the unit time.
    :param u: the service rate of each automatic counter
    :return: machine_check_time
    """
    factorial = lambda n : 1 if n == 0 else factorial(n - 1) * n
    k = 5
    rho = l / u
    P_0 = 1. / ((rho**k)/(1-rho)/factorial(k) + sum((rho**i)/factorial(i) for i in range(k)))
    w_q = ((k*rho)**k)*rho*P_0/factorial(k)/((1-rho)**2)/l
    return w_q


class Passenger:
    def __init__(self, time:int):
        """
        initialize passengers waiting for security check
        :param time: record the time that passengers get in the security check queue """
        self.in_time = time
        self.passengers = random.randrange(0, 6)
        self.holiday_passengers = random.randrange(0, 11)
        # time of new passenger getting into queue TBD - to be decided
        self.has_luggage = round(np.random.binomial(1, 0.7))

    def get_passengers(self):
        """
        :return: number of passengers waiting in the security check queue"""
        return self.passengers

    def get_holidays_passengers(self):
        """
        Compared with get_passengers, it returns passengers in scenario
        :return: number of passengers in holidays waiting in the security check queue
        """
        return self.holiday_passengers

    def wait_time(self, out_time:int):
        """
        :return: calculate the wait time by recording in timestamp and out timestamp
        """
        return out_time - self.in_time

    def check_luggage(self):
        """
        randomly simulate the passengers whether have luggage or not. If so, add luggage check time to the total wait time.
        :return: luggage check time
        """
        has_luggage = self.has_luggage
        if has_luggage == 1:
            return math_automatictime(40, 0.9)
        elif has_luggage == 0:
            return 0

    def check_holidays_luggage(self):
        """
        randomly simulate the passengers whether have luggage or not. If so, add luggage check time to the total wait time.
        :return: luggage check time
        """
        has_luggage = self.has_luggage
        if has_luggage == 1:
            return math_automatictime(5, 0.8)
        elif has_luggage == 0:
            return 0


class CheckCounter:
    def __init__(self,time_per_passenger:int):
        """ initialize the security check counters
        :param time_per_passenger: time_per_passenger """
        self.time_per_passenger = time_per_passenger
        self.current_passenger = None
        # record the current passenger
        self.remaining_time = 0
        # record the remaining security check time for current passenger

    def is_busy(self):
        """check whether the check counter has passengers in check or not
        :return: whether the current checking counter is busy or not """
        return self.current_passenger != None

    def load_passenger(self, next_passenger, second):
        """ load new passenger """
        self.current_passenger = next_passenger
        self.remaining_time = next_passenger.get_passengers()*self.time_per_passenger
        if len(bus_arrtimes):
            for j in bus_arrtimes:
                if second == j:
                    self.remaining_time += 50*self.time_per_passenger
        # re-calculate the new remaining time

    def load_holiday_passenger(self, next_passenger, second):
        """ load new passenger in holiday scenario """
        self.current_passenger = next_passenger
        self.remaining_time = next_passenger.get_holidays_passengers() * self.time_per_passenger
        if len(bus_arrtimes):
            for j in bus_arrtimes:
                if second == j:
                    self.remaining_time += 50 * self.time_per_passenger

    def check_passenger(self):
        """ security check passengers """

        if self.is_busy(): # if there is passengers waiting to be checked
            self.remaining_time -= 1
            # the number of waiting passengers minus one after finishing  checking for a passenger
            if self.remaining_time <= 0:
                # if the security check has finished
                self.current_passenger = None
        else:  # if there is no passengers waiting to be checked
            pass


def simulate(total_time:int, time_per_passenger:int)->float:
    """ simulate the airport security check in non_holiday scenario
    :param total_time: total security check duration
    :param time_per_passenger: record checking time for each passengers
    :param checktime: the time of security check for each passenger """
    waiting_time = []
    # record waiting time for each passenger
    luggage_time = []

    check_counter = CheckCounter(time_per_passenger)
    wait_line = CheckQueue()

    for second in range(total_time):

        rand_num = random.randrange(1, 101)
        # TBD: for 5 counters checking 180 passengers per hour, one passenger can be checked in 100 seconds.
        if rand_num == 1:
            new_passenger = Passenger(second)
            wait_line.enqueue(new_passenger)
            # new passengers get in queue

        if (not check_counter.is_busy()) and (not wait_line.isEmpty()):
            # if there is a not busy counter while passengers wait in line.
            next_passenger = wait_line.dequeue()
            waiting_time.append(new_passenger.wait_time(second))
            # calculate and record the waiting time
            luggage_time.append(new_passenger.check_luggage())
            check_counter.load_passenger(next_passenger,second)
            # if bus_arrtimes > 0:

        check_counter.check_passenger()

    average_time = sum(waiting_time)/len(waiting_time)
    total_waittime = average_time + sum(luggage_time)

    return total_waittime


def holiday_simulate(total_time:int, time_per_passenger:int)->float:
    """ simulate the airport security check in holiday scenario
    :param total_time: total security check duration
    :param time_per_passenger: record checking time for each passengers
    :param checktime: the time of security check for each passenger """
    waiting_time = []
    # record waiting time for each passenger
    luggage_time = []

    check_counter = CheckCounter(time_per_passenger)
    wait_line = CheckQueue()

    for second in range(total_time):

        rand_num = random.randrange(1, 201)
        if rand_num == 1:
            new_passenger = Passenger(second)
            wait_line.enqueue(new_passenger)

        if (not check_counter.is_busy()) and (not wait_line.isEmpty()):
            next_passenger = wait_line.dequeue()
            waiting_time.append(new_passenger.wait_time(second))
            luggage_time.append(new_passenger.check_holidays_luggage())
            check_counter.load_holiday_passenger(next_passenger,second)

        check_counter.check_passenger()

    average_time = sum(waiting_time)/len(waiting_time)
    total_waittime = average_time + sum(luggage_time)

    return total_waittime

def getuserdate()-> str:
    """ get the user planned date and time period of arriving the airport, which may or may not include the year.
    :return: return the user input date
    """
    command = input(
        "Enter the estimated time range (06.00 10.00 Dec.15) or (06.00 10.00 Dec.15 2018):")
    # Dec.20 07.00 09.00 terminal1
    # command = 'terminal1 08.00 10.00 Dec.15'
    commandList = command.split()
    if len(commandList) < 3 or len(commandList) > 4:
        sys.exit(0)
    starttime = commandList[0]
    endtime = commandList[1]
    date = commandList[2]
    if len(commandList) == 4:
        year = commandList[3]
    else:
        year = 2017
    monthDict = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6, "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10,
                 "Nov": 11, "Dec": 12}
    month, day = date.split('.')
    for keys in monthDict.keys():
        if keys == month:
            month = monthDict[keys]
    # Get the weekday of the data user input
    weekday = calendar.day_name[datetime.datetime(int(year), int(month), int(day)).weekday()]

    bus_schedule = pd.read_csv('bus_schedule.csv', sep=',')
    bus_schedule = bus_schedule.fillna('')  # replace all the nan as ''

    timeList = []
    bustime = ''
    indexpos = 0
    for i in bus_schedule['holiday_date']:
        if i == date or i == weekday:
            timeList.append(indexpos)
        indexpos += 1

    if len(timeList):
        for i in timeList:
            bustime += ' '
            bustime += bus_schedule.loc[i, 'schedule']

    global bus_arrtimes
    bus_arrtimes = []
    for i in bustime.split(' '):
        if i[0:2] == starttime[0:2]:
            if int(i[3:5]) >= int(starttime[3:5]):
                bus_arrtimes.append(int(i[3:5])-int(starttime[3:5]))
        elif i[0:2] == endtime[0:2]:
            if int(i[3:5]) <= int(endtime[3:5]):
                bus_arrtimes.append(60*(int(i[0:2]) - int(starttime[0:2])) + int(i[3:5]))
        elif starttime[0:2] < i[0:2] and i[0:2] < endtime[0:2]:
            bus_arrtimes.append(60 * (int(i[0:2]) - int(starttime[0:2])) + int(i[3:5]))

    return date


def main():
    time_per_passenger = 30
    # TBD: 100 is just for
    # current test
    total_time = 3600
    # TBD： 1 hour is just for current test
    while True:
        print("****************************")
        input_date = getuserdate()
        waittime_list = []
        christmas_period = {1: "Dec.23", 2 :"Dec.24", 3 :"Dec.25", 4 :"Dec.26", 5: "Dec.27"}
        label = 0
        times = []
        for value in christmas_period.values():
            if input_date == value:
                label = 1
        if label == 1:
            for i in range(20):
                total_waittime = holiday_simulate(total_time, time_per_passenger)
                waittime_list.append(total_waittime)
                times.append(i)
                print("****************************")
                print("The average waiting time for airport security check：%.2f s" % total_waittime)
        else:
            for i in range(20):
                total_waittime = simulate(total_time, time_per_passenger)
                waittime_list.append(total_waittime)
                times.append(i)
                print("****************************")
                print("The average waiting time for airport security check：%.2f s" % total_waittime)
        print("****************************")
        print("The waiting time is %.2f s" % min(waittime_list), "to %.2f s" % max(waittime_list))
        plt.ylim(0, 1500)
        plt.xlabel('Times')
        plt.ylabel('Average wait time(s)')
        plt.title('20 times average wait time')
        plt.scatter(times, waittime_list, alpha=0.6)

        plt.show()
        command = input("Do you wanna quit? Y/N: ")
        if command == "Y" or command == "y":
            print("Bye!")
            break
        elif command == "N" or command == "n":
            continue
        else:
            print("Wrong input! Try again:")
            continue

if __name__ == "__main__":
    main()

