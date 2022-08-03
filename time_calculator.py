def add_time(time, duration, day=None):

    time = time.split(' ')                  # start time
    splitted_time = time[0].split(':')
    hours = splitted_time[0]                # start hours
    minutes = splitted_time[1]              # start minutes
    splitted_duration = duration.split(':') # duration of time passed

    time_dict = {'0':12, '1':13,'2':14,'3':15,'4':16,'5':17,'6':18,'7':19,'8':20,'9':21,'10':22,'11':23, '12':12} # 24-Hour time format
    time_dict2 = {'0':12, '12':12,'13':1,'14':2,'15':3,'16':4,'17':5,'18':6,'19':7,'20':8,'21':9,'22':10,'23':11} # 12-Hour time format
    week = ['Monday', 'Tuesday', 'Wednesday','Thursday','Friday','Saturday', 'Sunday']
    
    if time[1] == 'AM':
        output_time = hours
    else:
        output_time = hours.replace(hours, str(time_dict[hours])) # convert time to 24-Hour time format

    new_hours = int(output_time) + int(splitted_duration[0])
    new_minutes = int(minutes) + int(splitted_duration[1])

    if new_minutes > 59:
        new_hours += 1
        new_minutes -= 60
    
    if len(str(new_minutes)) == 1:
        str(new_minutes)
        new_minutes = '0' + str(new_minutes)

    if day:
        new_day = f", {week[(week.index(day.lower().capitalize()) + (new_hours // 24)) % 7]}" # find out day of the week if day argument is given
    else:
        new_day = f""
    
    if new_hours > 24:
        full_days = new_hours // 24 # find out how much days had passed

        result = f"{new_hours - (full_days * 24)}:{new_minutes}"
        
        if result.startswith('0'):
            result = result.replace('0', '12', 1)
            
        result = result.split(':')
        
        if int(result[0]) <= 12:
            if full_days == 1:
                result = f"{result[0]}:{new_minutes} AM{new_day} (next day)"
                return result
            else:
                result = f"{result[0]}:{new_minutes} AM{new_day} ({full_days} days later)"
                return result

        if int(result[0]) > 12:
            result[0] = result[0].replace(result[0], str(time_dict2[result[0]]))
            
            if full_days == 1:
                result = f"{result[0]}:{new_minutes} PM{new_day} (next day)"
                return result
            else:
                result = f"{result[0]}:{new_minutes} PM{new_day} ({full_days} days later)"
                return result
    
    else:
        if new_hours < 12:
            result = f"{new_hours}:{new_minutes} AM{new_day}"
            return result
        else:
            output_time = str(new_hours).replace(str(new_hours), str(time_dict2[str(new_hours)]))
            result = f"{output_time}:{new_minutes} PM{new_day}"
            return result