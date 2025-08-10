def add_time(start_time, duration, day_of_week=None):
    start_parts = start_time.split( )
    time_part = start_parts[0]
    period = start_parts[1]
    
    hour_and_minute = time_part.split(':')
    start_hour = int(hour_and_minute[0])
    start_minute = int(hour_and_minute[1])

    duration_parts = duration.split(':')
    duration_hour = int(duration_parts[0])
    duration_minute = int(duration_parts[1])

    if period == 'PM' and start_hour != 12:
        start_hour += 12
    elif period == 'AM' and start_hour == 12:
        start_hour = 0

    total_minute = start_minute + duration_minute

    carry_over_hours= total_minute // 60
    final_minute = total_minute % 60

    total_hours_sum = start_hour + duration_hour + carry_over_hours

    days_later = total_hours_sum // 24
    final_hour_24_format = total_hours_sum % 24


    result_period = ''

    if final_hour_24_format >= 12:
        result_period = 'PM'
        if final_hour_24_format > 12:
            final_hour_12 = final_hour_24_format - 12
        else:
            final_hour_12 = 12
    else:
        result_period = 'AM'
        if final_hour_24_format == 0:
            final_hour_12 = 12
        else:
            final_hour_12 = final_hour_24_format

    final_minute_str = f'{final_minute:02d}'

    new_time = f'{final_hour_12}:{final_minute_str} {result_period}'

    if day_of_week:
        days_of_the_week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        start_day_index = days_of_the_week.index(day_of_week.lower()) 
        new_day_index = (start_day_index + days_later) % 7 
        final_day = days_of_the_week[new_day_index] 
        new_time += f', {final_day.title()}'

    if days_later == 1:
        new_time += ' (next day)'
    elif days_later > 1:
        new_time += f' ({days_later} days later)'


    return new_time
