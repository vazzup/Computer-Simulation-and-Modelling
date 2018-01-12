#!/usr/bin/env python3
class Event:
    NAME, TIME, TRUCK_NO = "", 0, -1
    def __init__(self, name = "", time = 0, truck_no = -1):
        this.NAME =  name
        this.TIME = time
        this.TRUCK_NO = truck_no
    
    def __lt__(self, other):
        return self.TIME < other.TIME
    
    def __le__(self, other):
        return self.TIME <= other.TIME

    def __gt__(self, other):
        return self.TIME > other.TIME
    
    def __ge__(self, other):
        return self.TIME >= other.TIME
    
    def __eq__(self, other):
        return self.TIME == other.TIME

    def __ne__(self, other):
        return self.TIME != other.TIME

class EventConst:
    EL = "End Loading"
    ALQ = "Arrive at Loading Queue"
    EW = "End Weighing"

def main():
    from queue import Queue, PriorityQueue
    number_trucks = int(input('Enter number of trucks'))
    number_scales = int(input('Enter number of scales'))
    number_loaders = int(input('Enter number of loaders'))
    load_time_size = int(input('Enter size of loading time array'))
    weight_time_size = int(input('Enter size of weighing time array'))
    travel_time_size = int(input('Enter size of travelling time array'))
    load_time = list(map(int, input('Enter the loading time array')\
                        .strip().split()))
    weight_time = list(map(int, input('Enter the weighing time array')\
                        .strip().split()))
    travel_time = list(map(int, input('Enter the travelling time array')\
                        .strip().split()))
    load_time_index, weight_time_index, travel_time_index = 0, 0, 0
    busy_time_loader, busy_time_scale = 0, 0
    future_event_list = PriorityQueue()
    loader_queue, scale_queue = Queue(), Queue()
    loader_wait_queue, scale_wait_queue = Queue(), Queue()
    current_time = 0
    for i in range(1, min(number_scales + 1, number_trucks + 1)):
        scale_queue.put(i)
        future_event_list.put(Event(EventConst.EW, current_time + weight_time[weight_time_index], i))
    for i in range(scales+1, min(number_loaders + number_scales + 1, number_trucks)):
        loader_queue.put(i)
        future_event_list.put(Event(EventConst.EL, current_time + load_time[load_time_index], i))
    return

if __name__ == '__main__':
    main()
