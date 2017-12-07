import pandas as pd

command  = input("Type in the time range and the terminal here please(Dec.20 07.00 09.00 terminal1):")
      # if len(command) < 1:#check prevents a crash when indexing to 1st character
      #    continue
commandList = command.split()
date = commandList[0]
starttime = commandList[1]
endtime = commandList[2]
terminal = commandList[3]
bus_schedule = pd.read_csv('bus_schedule.csv',sep=',')
bus_schedule = bus_schedule.fillna('') # replace all the nan as ''
# print(bus_schedule['holiday_date'== date])
# print(bus_schedule['holiday_date'].get_loc(date))
timeList = []
bustime = ''
indexpos = 0
for i in bus_schedule['holiday_date']:
    if i == date:
        # print(indexpos)
        timeList.append(indexpos)
    indexpos += 1

if len(timeList):
    for i in range(len(timeList)):
        # timeList[i] = bus_schedule.loc[i,'schedule']
        # print((bus_schedule.loc[i, 'schedule']))
        bustime += ' '
        bustime += bus_schedule.loc[i, 'schedule']
        # bustime.append(timeList[i].split(','))

        # print(bus_schedule.loc[i,'schedule'])
        #  print(bus_schedule)
#print(bustime)
bus_arrtime = ''
for i in bustime.split(' '):
    if i[0:2]== starttime[0:2]:
        if int(i[3:5]) >= int(starttime[3:5]):
            bus_arrtime += (i + ' ')
    elif i[0:2]== endtime[0:2]:
        if int(i[3:5]) <= int(starttime[3:5]):
            bus_arrtime += (i + ' ')
    elif starttime[0:2] <= i[0:2] and i[0:2] <= endtime[0:2]:
        bus_arrtime += (i + ' ')

# Print the time buses would come during the time range users have set
print(bus_arrtime)

