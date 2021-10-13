import theaterSeats
import os

def main():
    # First, we take the input file.
    print("Please specify the input file:")
    inputFile = input()
    try:
        with open(inputFile, 'r') as f:
            lines = f.readlines()
    except IOError as e:
        print("I/O error({0}): {1}".format(e.errno, e.strerror))
        exit()
    except:
        print("Unexpected error:", sys.exc_info()[0])
        exit()

    reservations = []
    for line in lines:
        line = line.split(' ')
        reservations.append([line[0], int(line[1])])

    seats = theaterSeats.theaterSeats()
    for reservation in reservations:
        if not seats.allocateSeats(reservation[0], reservation[1]):
            print("The reservation for {} is not successful! Only {} seats left!".format(reservation[0], seats.getAvailability()))

    validReserves = seats.getValidReservation()
    outputFile = os.getcwd() + '/output.txt'
    with open(outputFile, 'w') as f:
        for line in validReserves:
            f.write(line)
            f.write('\n')
    print("Output: {}".format(outputFile))

    # seats.printSeats()




if __name__ == '__main__':
    main()
