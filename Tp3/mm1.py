import random
import math as m

busy = 1
idle = 0
q_limit = 100
next_event_type,num_custs_delayed, num_delays_required, num_events, num_in_q, server_status = 0, 0, 0, 0, 0, 0
area_num_in_q, area_server_status, mean_interarrival, mean_service, time, time_last_event, total_of_delays = 0, 0, 0, 0, 0, 0, 0
time_arrival = []
time_next_event = [0, 0, 0] 

def initialize():
    time = 0
    server_status = idle
    num_in_q = 0
    time_last_event = 0
    num_custs_delayed = 0
    total_of_delays = 0
    area_num_in_q = 0
    area_server_status = 0

    time_next_event[1] = time + expon(mean_interarrival) 
    time_next_event[2] = 10 ** 30

def timing():
    
    min_time_next_event = 10 ** 29
    next_event_type = 0

    for i in range(1, num_events + 1):
        if (time_next_event[i] < min_time_next_event):
            min_time_next_event = time_next_event[i]
            next_event_type     = i
    if next_event_type == 0:
        print("Event list empty")
        return
    time = min_time_next_event

def arrive():
    delay = 0
    time_next_event[1] = time + expon(mean_interarrival)

    if server_status == busy:
        num_in_q += 1
        if num_in_q > q_limit:
            print("Queue Overflow")
            return
        time_arrival[num_in_q] = time
    else:
        num_custs_delayed += 1
        server_status = busy 
        time_next_event[2] = time + expon(mean_service)

def depart():
    i = 0
    delay = 0
    if num_in_q == 0:
        server_status = idle
        time_next_event[2] = 10 ** 30
    else:
        num_in_q -= 1 
        delay = time - time_arrival[1]
        total_of_delays += delay

        num_custs_delayed += 1
        time_next_event[2] = time + expon(mean_service)
        for i in enumerate(time_arrival):
            time_arrival[i] = time_arrival[ i + 1]

def report():
    print(f"Average delay in queue {total_of_delays / num_custs_delayed}")
    print(f"Average number in queue {area_num_in_q / time}")
    print(f"Server utilization {area_server_status / time}")
    print(f"Time simulation ended {time}")


def update_time_avg_stats():
    time_since_last_event = 0

    time_since_last_event = time - time_last_event
    time_next_event = time
    area_num_in_q += num_in_q * time_since_last_event
    area_server_status += server_status * time_since_last_event

def expon(mean):
    r = random.random()
    x = -mean * m.log(r)
    return x

if __name__ == "__main__":
    num_events = 2
    
    #Leer mean_interarrival, mean_service, num_delays_required
    mean_interarrival = 1
    mean_service = 0.5
    num_delays_required = 1000

    #initialize()
    time = 0
    server_status = idle
    num_in_q = 0
    time_last_event = 0
    num_custs_delayed = 0
    total_of_delays = 0
    area_num_in_q = 0
    area_server_status = 0

    time_next_event[1] = time + expon(mean_interarrival) 
    time_next_event[2] = 10 ** 30
    
    while (num_custs_delayed < num_delays_required):
        timing()

        update_time_avg_stats()

        if next_event_type == 1:
            arrive()
        elif next_event_type == 2:
            depart()
    report()

