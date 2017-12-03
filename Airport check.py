import random


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
        :return:
        """
        length = len(self.items)
        return length


class Passenger:
    def __init__(self, time):
        """ initialize passengers waiting for security check
        :param time: record the time that passengers get in the security check queue """
        self.in_time = time
        self.passengers = random.randrange(1,11)
        # TBD - to be decided

    def get_passengers(self):
        """:return: number of passengers waiting in the security check queue"""
        return self.passengers

    def wait_time(self, out_time):
        """ :return: calculate the wait time by recording in timestamp and out timestamp """
        return out_time - self.in_time


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

    def load_passenger(self, next_passenger):
        """ load new passenger """
        self.current_passenger = next_passenger
        self.remaining_time = next_passenger.get_passengers()*self.time_per_passenger
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
    """ simulate the airport security check
    :param total_time: total security check duration
    :param time_per_passenger: record waiting time for each passengers """
    waiting_time = []
    # record waiting time for each passenger

    check_counter = CheckCounter(time_per_passenger)
    wait_line = CheckQueue()

    for second in range(total_time):

        rand_num = random.randrange(1, 101)
        # TBD: for 5 counters checking 180 passengers per hour, one passenger can be checked in 100 seconds.
        if rand_num == 1:
            new_passenger = Passenger(second)
            wait_line.enqueue(new_passenger)
            # new passenger get in queue

        if (not check_counter.is_busy()) and (not wait_line.isEmpty()):
            # if there is a not busy counter while passengers wait in line.
            next_passenger = wait_line.dequeue()
            waiting_time.append(new_passenger.wait_time(second))
            # calculate and record the waiting time
            check_counter.load_passenger(next_passenger)

        check_counter.check_passenger()

    average_time = sum(waiting_time)/len(waiting_time)
    return average_time


def main():
    time_per_passenger = 100
    # TBD: 100 is just for current test
    total_time = 3600
    # TBD： 1 hour is just for current test
    print("****************************")
    for i in range(5):
        average_time = simulate(total_time, time_per_passenger)
        print("The average waiting time for airport security check：%.5f s" % average_time)
        print("****************************")

if __name__ == "__main__":
    main()

