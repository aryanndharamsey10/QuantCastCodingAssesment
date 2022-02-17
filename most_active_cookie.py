import sys              # to get command line args
import datetime

DATE_FORMAT = "%Y-%m-%d"    #initializing correct date formatted

class CookieMonster:
    def __init__(self):                 #initializing a dictionary that will store all the cookies
        self.calendar = {}
        self.raw_data = []

    def open_file(self, file_name):         #opening file, returning error if the file cannot be opened
        try:
            return open(file_name, "r")
        except:
            raise Exception("Cannot open file")


    def parse_date(self, timestamp):
        date_str, time_str = timestamp.split("T")      #removing the time stamp from the line, since all times are in the same timezone the time characteristic is pointless, we only need a date
        return date_str

    def ingest_data(self, file_ptr):
        for line in file_ptr.readlines():
            self.raw_data.append(line)

    def parse_data(self):                                  #filling dictionary with relevant information by parsing the file
        for line in self.raw_data:
            # to get rid of any excess whitespace
            line = line.strip()
            # split based on the comma
            cookie, timestamp = line.split(",")
            date_str = self.parse_date(timestamp)

            if date_str not in self.calendar:
                self.calendar[date_str] = {}

            if cookie not in self.calendar[date_str]:
                self.calendar[date_str][cookie] = 0

            self.calendar[date_str][cookie] += 1

    def find_most_used(self, current_date):         #function that finds the most used cookie by parsing through the dictionarys key, value pairs. adds them to the list if they are the max occured
        date_log = self.calendar[current_date]
        max_occurances = 0
        max_occured_cookies = []

        for cookie in date_log.keys():

            if date_log[cookie] > max_occurances:
                max_occured_cookies = []
                max_occured_cookies.append(cookie)
                max_occurances = date_log[cookie]
            elif date_log[cookie] == max_occurances:
                max_occured_cookies.append(cookie)
        return max_occured_cookies


    def run(self, file_name, current_date):
        file_ptr = self.open_file(file_name)
        self.ingest_data(file_ptr)
        self.parse_data()

        for cookie in self.find_most_used(current_date):
            print(cookie)


# to avoid running the app in case file is imported as a module
# help section
if __name__ == "__main__":

    if sys.argv[1] == "-help":
        print("Most Active Cookie App: finds the most active cookie based on input csv and date\
              \nUsage: python3 most_active_cookie.py <file> -d <date>\
              \n \t\t <file> : csv file with the log of cookies\
              \n \t\t <date> : query date for most active cookie in the format YYYY-MM-DD (UTC)")
        exit()
    # if optional testing args are provided through the command line
    if len(sys.argv) == 4 and sys.argv[1] and sys.argv[2] and sys.argv[3]:
        if sys.argv[2] == "-d":
            try:
                datetime.datetime.strptime(sys.argv[3], DATE_FORMAT)
                app = CookieMonster()
                app.run(sys.argv[1], sys.argv[3])
            except ValueError:
                print("\nProvided date string is in incorrect format. Please use the -help flag for more information.\n")

    else:
        print("\nIncorrect usage, try running with -help flag to get more information on how to run the program.\n")
        exit()



