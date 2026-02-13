## Student Name: Amin Hosseini
## Student ID: 218926840

"""
Stub file for the meeting slot suggestion exercise.

Implement the function `suggest_slots` to return a list of valid meeting start times
on a given day, taking into account working hours, and possible specific constraints. See the lab handout
for full requirements.
"""
from typing import List, Dict

def suggest_slots(
    events: List[Dict[str, str]],
    meeting_duration: int,
    day: str
) -> List[str]:
    """
    Suggest possible meeting start times for a given day.

    Args:
        events: List of dicts with keys {"start": "HH:MM", "end": "HH:MM"}
        meeting_duration: Desired meeting length in minutes
        day: Three-letter day abbreviation (e.g., "Mon", "Tue", ... "Fri")

    Returns:
        List of valid start times as "HH:MM" sorted ascending
    """
    # TODO: Implement this function
    #Assuming the slots occur every 15 minutes
    list_of_slots = [(15*i)+540 for i in range(0, 32)] 
    list_of_slots = [x for x in list_of_slots if x<720 or x>780]
    list_of_avail_slots = []
    for start_time in list_of_slots:
        cond = 0
        end_time = start_time + meeting_duration
        print(f"{start_time} to {end_time}")
        if end_time <= 1020:
            for event in events:
                print(event)

                if convert_time_to_mins(event['start']) > 0 and convert_time_to_mins(event['end']) > 0:
                    if not convert_time_to_mins(event['start']) >= end_time and not convert_time_to_mins(event['end']) < start_time:
                        cond = 1
                    print(f"{start_time} with {meeting_duration} not is available due to {event} \n")
                    print(not convert_time_to_mins(event['start']) >= end_time and not convert_time_to_mins(event['end']) <= start_time)
                else:
                    if not convert_time_to_mins(event['start']) >= end_time and not convert_time_to_mins(event['end']) < start_time:
                        cond = 1
                    print(f"{start_time} with {meeting_duration} not is available due to {event} \n")
            if cond == 0:
                list_of_avail_slots.append(f'{start_time//60:02d}:{start_time%60:02d}')
    print(list_of_avail_slots)
    return list_of_avail_slots

def convert_time_to_mins(date_str : str) -> int:
    str = date_str.split(':')
    hour = str[0]
    minute = str[1]
    if int(hour) > 24 or int(minute) > 60 or int(hour) <0 or int(minute) < 0:
        return -5
    return (int(hour) * 60) + int(minute)
