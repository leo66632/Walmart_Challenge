**Movie Theater Seating Challenge**

**Assumptions:**
1. Reservation request that comes earlier has higher priority. That is to say, when a new request cannot be accommodate, the program will deny the request rather than modify prior reservations to fit the new one.
2. If a request cannot be accommodated, the program simply skip it with a declining message. Then, the program move on and handle later requests.
3. For public safety, we maintain a buffer of three seats and one row for each occupied seat. This is illustrated below:
    X X X X X X X
    X X X O X X X
    X X X X X X X
   For an occupied seat "O", the surrounding seats "X"s cannot be seated.
4. However, people from the same group are not subjected to this regulation. Thus, seats accommodated for the same request can be arranged together.
5. For customer satisfaction, the program will try to accommodate the same group of people in the same row and adjacent seats. If not possible, the program will try to placed the group in adjacent rows.
6. Similarly, the program will not modify prior reservations so that the new reservation can be allocated in the same row.
7. The reservations in the input file have sequential order.

**Execution:**
1. Download the entire folder and unzip it.
2. Navigate into the folder where "main.py" is stored.
3. Run the following command: python3 main.py
4. Type in the full path of the input file. For example: /Users/USER_NAME/Walmart_Challenge/test.txt
5. The program generate the output file and print the full path of it.
