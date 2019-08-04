import sys

class classInfo:
    def __init__(self, day, start, end, room):
        self.day = day
        self.start = start
        self.end = end
        self.room = room


def vacant(startPair, endPair, targetHour, targetMinutes):

	if (startPair[0]<targetHour)  and (endPair[0]>=targetHour):

		if (int(startPair[1])< targetMinutes) or (int(endPair[1])>=targetMinutes):
			return 1
		elif (int(startPair[1])<= targetMinutes) or (int(endPair[1])>targetMinutes):
			return 1	
		else:	
			return 0

	elif (startPair[0]<targetHour) and (endPair[0]>targetHour):
	
		if (int(startPair[1])< targetMinutes) or (int(endPair[1])>=targetMinutes):
			return 1
		elif (int(startPair[1])<= targetMinutes) or (int(endPair[1])>targetMinutes):
			return 1	
		else:	
			return 0

	elif (startPair[0]<=targetHour) and (endPair[0]>targetHour):
	
		if (int(startPair[1])< targetMinutes) or (int(endPair[1])>=targetMinutes):
			return 1
		elif (int(startPair[1])<= targetMinutes) or (int(endPair[1])>targetMinutes):
			return 1	
		else:	
			return 0
	
	elif (startPair[0]<=targetHour) and (endPair[0]>=targetHour):
		
		if (int(startPair[1])< targetMinutes) or (int(endPair[1])>=targetMinutes):
			return 1
		elif (int(startPair[1])<= targetMinutes) or (int(endPair[1])>targetMinutes):
			return 1	
		else:	
			return 0
			
	else:
		return 0


def createList():
	file = open("fall2019.txt", "r")

	LIV = []
	CAC = []
	BUS = []
	CookDoug = []


	for line in file:

		word = line.split()

		day = word[0]

		startTime = word[1].split(":")
		startHour = int(startTime[0])
		startMinutes = startTime[1]

		if (word[2] == "AM" or startHour == 12):

			startPair = [startHour, startMinutes]
		else:
			startHour = startHour + 12
			startPair = [startHour, startMinutes]

	
		endTime = word[4].split(":")
		endHour = int(endTime[0])
		endMinutes = endTime[1]


		if (word[5] == "AM" or endHour == 12):
			endPair = [endHour, endMinutes]
		else:
			endHour = endHour + 12
			endPair = [endHour, endMinutes]

		
		campus = word[6]


		try:
			room = word[7]
		except:
			continue 

		if campus == "LIV":
			LIV.append(classInfo(day, startPair, endPair, room))
		elif campus == "CAC":
			CAC.append(classInfo(day, startPair, endPair, room))
		elif campus == "BUS":
			BUS.append(classInfo(day, startPair, endPair, room))
		elif campus == "D/C":
			CookDoug.append(classInfo(day, startPair, endPair, room))

	finalList = [LIV,CAC,BUS,CookDoug]

	return finalList

def updateUntil(startPair, xhour, xminutes, targetHour, targetMinutes):
	if (startPair[0] == targetHour) and (startPair[1] > targetMinutes):
		if (startPair[0]==xhour and (startPair[1]<xminutes)) :
			return 1

		elif (startPair[0]<xhour):
			return 1
	
	elif (startPair[0] > targetHour):
		if (startPair[0]==xhour) and (startPair[1]<xminutes):	
			return 1
		elif (startPair[0]<xhour):	
			return 1
	return 0



def modifyList(x, targetCampus,day, targetHour, targetMinutes):
	for y in targetCampus:

			if (y.room in x) and (y.day == day):
				line = x.split()
				roomNum = line[0]
				
				try: 
					time = line[3]
					spl = time.split(":")
					xhour = int(spl[0])
					xminute = spl[1]
					
					if line[4] == 'pm':
						if xhour != 12:
							xhour = xhour + 12
							
					if updateUntil(y.start, xhour, xminute, targetHour,targetMinutes) == 1:
						xhour = y.start[0]
						xminute = y.start[1]

						if xhour > 12:
							xhour = xhour - 12
							xminute = str(y.start[1]) + " pm "
						elif xhour == 12:
							xminute = str(y.start[1]) + " pm "
						else:
							xminute = str(y.start[1]) + " am "

						x = roomNum + "          open until:       " + str(xhour) + ":" + str(xminute) + y.day

				except:

					if (y.start[0] > targetHour and int(y.start[1]) >= int(targetMinutes)) or (y.start[0] >= targetHour and int(y.start[1]) > int(targetMinutes) ):
						xhour = y.start[0]

						if xhour > 12:
							xhour = xhour - 12
							xminute = str(y.start[1]) + " pm "
						elif xhour == 12:
							xminute = str(y.start[1]) + " pm "						
						else:
							xminute = str(y.start[1]) + " am "

						x = roomNum + "          open until:       " + str(xhour) + ":" + str(xminute) + y.day

	return x				

					

def addRoomLinks(lst):

	roomInfo = open("spring2019rmInfo.txt", "r")

	roomLinks = []

	for line in roomInfo:
		roomLinks.append(line)

	retLst = []
	for x in lst:
		
		try:
			split = x.split("-")
			name = split[0]
			roomWithLink = ([x for x in roomLinks if name == x.split()[0]][0].split()[1], x )
			retLst.append(roomWithLink)
		except:
			continue

	return retLst				
					

		
def checkTime(campus, day, hour, minutes):

	lst = createList()

	if campus == "College Ave":
		targetCampus = lst[1]
	elif campus == "Livingston":
		targetCampus = lst[0]
	elif campus == "Busch":
		targetCampus = lst[2]
	elif campus == "Cook/Douglass":
		targetCampus = lst[3]

	openRooms = []

	for x in targetCampus:

		if x.room not in openRooms:
			openRooms.append(x.room)


	for x in targetCampus:

		if (x.day == day and vacant(x.start, x.end, hour, minutes)==1):
			
			if x.room in openRooms:
				openRooms.remove(x.room)

	retList = []				

	for x in openRooms:
		
		retList.append(modifyList(x,targetCampus,day,hour,minutes))

	
	printList = []
	for x in retList:

		line = x.split()

		try:
			time = line[3]
			printList.append(x)
		except:
			x = x + "          open rest of the day      " 
			printList.append(x)	
 
	return addRoomLinks(sorted(printList))



	