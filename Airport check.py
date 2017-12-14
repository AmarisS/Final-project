import random
import numpy as np
import pandas as pd
import datetime
import calendar

class CheckQueue():
    def __init__(self):
        """ create an empty queue """
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
    def __init__(self, time):
        """ initialize passengers waiting for security check
        :param time: record the time that passengers get in the security check queue """
        self.in_time = time
        self.passengers = random.randrange(0, 6)
        # time of new passenger getting into queue TBD - to be decided
        self.has_luggage = round(np.random.binomial(1, 0.7))

    def get_passengers(self):
        """:return: number of passengers waiting in the security check queue"""
        return self.passengers

    def wait_time(self, out_time):
        """ :return: calculate the wait time by recording in timestamp and out timestamp """
        return out_time - self.in_time

    def check_luggage(self):
        has_luggage = self.has_luggage
        if has_luggage == 1:
            return math_automatictime(20, 0.9)
        elif has_luggage == 0:
            return 0


class CheckCounter:
    def __init__(self,time_per_passenger):
        """ initialize the security check counters
        :param time_per_passenger: time_per_passenger """
        self.time_per_passenger = time_per_passenger
        self.current_passenger = None
        # record the current passenger
        self.remaining_time = 0
        # record the remaining security check time for current passenger

    def is_busy(self):
        """:return: whether the current checking counter is busy(have passenger in check) or not """
        return self.current_passenger != None

    def load_passenger(self, next_passenger,second):
        """ load new passenger """
        self.current_passenger = next_passenger
        self.remaining_time = next_passenger.get_passengers()*self.time_per_passenger
        if len(bus_arrtimes):
            for j in bus_arrtimes:
                if second == j:
                    self.remaining_time += 50*self.time_per_passenger
        # re-calculate the new remaining time

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


def simulate(total_time, time_per_passenger):
    """ simulate the airport security check in non_holiday scenario
    :param total_time: total security check duration
    :param time_per_passenger: record checking time for each passengers """
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
    #print("waitingtime",sum(waiting_time))
    #print("waitinelength",len(waiting_time))
    #print("luggagetime:",sum(luggage_time))
    return total_waittime

def simulate_holiday(total_time, time_per_passenger):
    """ simulate the airport security check in holidays
       :param total_time: total security check duration
       :param time_per_passenger: record checking time for each passengers """
    waiting_time = []
    luggage_time = []

    check_counter = CheckCounter(time_per_passenger)
    wait_line = CheckQueue()

    for second in range(total_time):

        rand_num = random.randrange(1, 181)
        # In holiday scenario, the time one passenger can be checked would be longer -- in 180 seconds.
        if rand_num == 1:
            new_passenger = Passenger(second)
            wait_line.enqueue(new_passenger)

        if (not check_counter.is_busy()) and (not wait_line.isEmpty()):
            next_passenger = wait_line.dequeue()
            waiting_time.append(new_passenger.wait_time(second))
            # calculate and record the waiting time
            luggage_time.append(new_passenger.check_luggage())
            check_counter.load_passenger(next_passenger, second)

        check_counter.check_passenger()

    average_time = sum(waiting_time) / len(waiting_time)
    total_waittime = average_time + sum(luggage_time)
    return total_waittime

def getuserdate():
    """

    :return:
    """
    command = input(
        "Type in the time range and the terminal here please(terminal1 06.00 10.00 Dec.15) or (terminal1 06.00 10.00 Dec.15 2018):")
    # Dec.20 07.00 09.00 terminal1
    # command = 'terminal1 08.00 10.00 Dec.15'
    commandList = command.split()
    terminal = commandList[0]
    starttime = commandList[1]
    endtime = commandList[2]
    date = commandList[3]
    if len(commandList) > 4:
        year = commandList[4]
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

def main():
    time_per_passenger = 30
    # TBD: 100 is just for
    # current test
    total_time = 3600
    # TBD： 1 hour is just for current test
    print("****************************")
    input_date = getuserdate()
    print(input_date)
    waittime_list = []
    # record the waittime list for several times simulation
    for i in range(8):
        if (input_date == 'Dec 25'):
            total_waittime = simulate_holiday(total_time,time_per_passenger)
        else:
            total_waittime = simulate(total_time, time_per_passenger)
        waittime_list.append(total_waittime)
        print("****************************")
        print("The average waiting time for airport security check：%.2f s" % total_waittime)
        #actual_passenger = np.random.poisson(180, 1)
    print("****************************")
    print("The waiting time is %.2f s" % min(waittime_list), "to %.2f s" % max(waittime_list))
    # print(math.ceil(total_time / actual_passenger * 5))
    #     print(average_time + math.ceil(total_time / actual_passenger * 5))

if __name__ == "__main__":
    main()
