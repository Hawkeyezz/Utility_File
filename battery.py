import psutil

battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = battery.percent

if percent <= 20 and plugged != True:
    # pip install py-notifier
    # pip install win10toast
    from pynotifier import Notification
    
    Notification(
    title="Low Battery Warning",
    description=str(percent) + "% Battery Remain!!",
    duration=5, # duration in seconds
    ).send()
