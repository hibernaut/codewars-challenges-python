import re


# Main function
def subs_offset_apply(subtitle, offset):
    offset_limit = 359999999

    # Splitting array into start time and stop time
    splitted_array = subtitle.split(' ')
    start_time = re.split(':|,', splitted_array[0])
    stop_time = re.split(':|,', splitted_array[2])

    # Calculating common time with offset in milliseconds
    common_start_time = calc_common_time(start_time, offset)
    common_stop_time = calc_common_time(stop_time, offset)

    # Checking if the value is correct
    if common_start_time < 0 or common_stop_time > offset_limit:
        return "Invalid offset"

    # Converting time into required format
    splitted_array[0] = convert_milliseconds(common_start_time)
    splitted_array[2] = convert_milliseconds(common_stop_time)

    return ' '.join(splitted_array)


# Function calculating common time with offset in milliseconds
def calc_common_time(array, offset):
    return (((int(array[0]) * 60 + int(array[1])) * 60 + int(array[2])) * 1000 + int(array[3])) + offset


# Function converting time in milliseconds into format "hh:mm:ss:msmsms"
def convert_milliseconds(time):
    h = int(time / 3600000)
    m = int((time - h * 3600000) / 60000)
    s = int((time - (h * 3600000 + m * 60000)) / 1000)
    ms = time - (h * 3600000 + m * 60000 + s * 1000)

    return "%02d:%02d:%02d,%03d" % (h, m, s, ms)
