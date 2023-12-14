
def format_time(total, speed=3800):
    minutes_left = total // speed

    minutes = minutes_left % 60
    hours = (minutes_left % (60 * 24)) // 60

    days =  minutes_left // (60*24)
    out_m = ""

    if days != 0:
        out_m += f"{days} days "

    if hours != 0:
        out_m += f"{hours} hours "

    out_m += f" {minutes} minutes left"

    return out_m
def format_seconds(s):
    hours, remainder = divmod(s, 3600)
    minutes, seconds = divmod(remainder, 60)
    return '{:02} hours {:02} mins {:02} secs'.format(int(hours), int(minutes), int(seconds))

if __name__ == "__main__":

    m = 6513881420
    print(format_time((m)))
