class theaterSeats:
    # initialization
    def __init__(self):
        # matrix of theater seats
        # a seat denoted as 's' is an available seat
        # a seat denoted as 'h' is an held seat (not available)
        self.theater = [['s' for i in range(20)] for j in range(10)]
        # availability, can be used to check if a request can be fullfiled
        self.availability = 200
        # availability by row, can be used to check whether a group can be placed in same row
        self.availabilityByLine = [20 for i in range(10)]
        # record all the successful reservations
        self.reservations = []

    # check if the current request can be accommodated by comparing the required seats and the availability
    def isAvailable(self, seatNum):
        if seatNum > self.availability:
            return False
        else:
            return True

    # the main logic to allocate seats
    def allocateSeats(self, reserveId, seatNum):
        # first check if the request can be fulfilled
        if not self.isAvailable(seatNum):
            return False
        else:
            # recorded all the seats arranged for the current request
            newReserved = []
            allocated = False
            # see if the seats can be arranged in the same row
            for row in range(10):
                if self.availabilityByLine[row] >= seatNum:
                    for col in range(20):
                        if self.theater[row][col] != 'h':
                            newReserved.append([row, col])
                            seatNum -= 1
                            if seatNum == 0:
                                break
                    allocated = True
                    break
            # if cannot allocate in the same row, try to allocate them in adjacent rows
            if not allocated:
                for row in range(10):
                    if self.availabilityByLine[row] > 0:
                        for col in range(20):
                            if self.theater[row][col] != 'h':
                                newReserved.append([row, col])
                                seatNum -= 1
                                if seatNum == 0:
                                    break
                        if seatNum == 0:
                            break
            # call "createBuffer" function to create buffer around this group of seats
            self.createBuffer(newReserved)
            # After successfuly accomodated the reservation, record it!
            confirmedReserve = reserveId + ' '
            for coord in newReserved:
                seat = chr(65 + coord[0]) + str(coord[1] + 1)
                confirmedReserve += (seat + ',')
            self.reservations.append(confirmedReserve[:-1])

            return True

    # create buffer for a (group of) reserved seats(s)
    # Also update the "availability" and the "availabilityByLine"
    def createBuffer(self, seats):
        for seat in seats:
            for r in range(-1,2,1):
                for c in range(-3,4,1):
                    newR = seat[0] + r
                    newC = seat[1] + c
                    if newR >= 0 and newR < 10 and newC >= 0 and newC < 20:
                        if self.theater[newR][newC] != 'h':
                            self.theater[newR][newC] = 'h'
                            self.availability -= 1
                            self.availabilityByLine[newR] -= 1

    # test functions
    def printSeats(self):
        for r in range(10):
            print(self.theater[r])

    def getValidReservation(self):
        return self.reservations

    def getAvailability(self):
        return self.availability
