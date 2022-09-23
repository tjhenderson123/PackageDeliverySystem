import Package


#ChainingHashTable from (Lysecky, Section 7.8)
# HashTable class using chaining.
class ChainingHashTable:
    # Constructor with optional initial capacity parameter.
    # Assigns all buckets with an empty list.
    #Run-time Complexity: Big O(n)
    def __init__(self, initial_capacity=41):
        # initialize the hash table with empty bucket list entries.
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # Inserts a new item into the hash table.
    # Run-time Big O(n)
    def insert(self, key, item):  # does both insert and update
        # get the bucket list where this item will go.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # update key if it is already in the bucket
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                kv[1] = item
                return True

        # if not, insert the item to the end of the bucket list.
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    # Searches for an item with matching key in the hash table.
    # Returns the item if found, or None if not found.
    #Run-time Big O(n)
    def search(self, key):
        # get the bucket list where this key would be.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        # print(bucket_list)

        # search for the key in the bucket list
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                return kv[1]  # value
        return None

    # Removes an item with matching key from the hash table.
    #Run-time Complexity Big O(n)
    def remove(self, key):
        # get the bucket list where this item will be removed from.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # remove the item from the bucket list if it is present.
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                bucket_list.remove([kv[0], kv[1]])

#Manually creating each package inside program
#Space Complexity Big O(n)
package1 = Package.Package(1, "195 W Oakland Ave", "Sacramento", "CA", "84115", "10:30 AM", 21, "N/A")
package2 = Package.Package(2, "2530 S 500 E", "Sacramento","CA","84106","EOD",44, "N/A")
package3 = Package.Package(3, "233 Canyon Rd", "Sacramento", "CA","84103","EOD",2,"Can only be on truck 2")
package4 = Package.Package(4, "380 W 2880 S", "Sacramento", "CA","84115","EOD",4, "N/A")
package5 = Package.Package(5, "410 S State St", "Sacramento", "CA","84111","EOD",5, "N/A")
package6 = Package.Package(6, "3060 Lester St", "Sacramento", "CA","84119","10:30 AM",88,"Delayed on flight---will not arrive to depot until 9:05 am")
package7 = Package.Package(7, "1330 2100 S", "Sacramento", "CA","84106","EOD",8, "N/A")
package8 = Package.Package(8, "300 State St", "Sacramento", "CA","84103","EOD",9, "N/A")
package9 = Package.Package(9, "300 State St", "Sacramento", "CA","84103","EOD",2,"Wrong address listed")
package10 = Package.Package(10, "600 E 900 South", "Sacramento", "CA","84105","EOD",1, "N/A")
package11 = Package.Package(11, "2600 Taylorsville Blvd", "Sacramento", "CA","84118","EOD",1, "N/A")
package12 = Package.Package(12, "3575 W Valley Central Station bus Loop", "Sacramento", "CA","84119","EOD",1, "N/A")
package13 = Package.Package(13, "2010 W 500 S", "Sacramento", "CA","84104","10:30 AM",2, "N/A")
package14 = Package.Package(14, "4300 S 1300 E", "Sacramento", "CA","84117","10:30 AM",88,"Must be delivered with 15, 19")
package15 = Package.Package(15, "4580 S 2300 E", "Sacramento", "CA","84117","9:00 AM",4, "N/A")
package16 = Package.Package(16, "4580 S 2300 E", "Sacramento", "CA","84117","10:30 AM",88, "Must be delivered with 13, 19")
package17 = Package.Package(17, "3148 S 1100 W", "Sacramento", "CA","84119","EOD",2, "N/A")
package18 = Package.Package(18, "1488 4800 S", "Sacramento", "CA","84123","EOD",6, "Can only be on truck 2")
package19 = Package.Package(19, "177 W Price Ave", "Sacramento", "CA","84115","EOD",37, "N/A")
package20 = Package.Package(20, "3595 Main St", "Sacramento", "CA","84115","10:30 AM",37, "Must be delivered with 13, 15")
package21 = Package.Package(21, "3595 Main St", "Sacramento", "CA","84115","EOD",3, "N/A")
package22 = Package.Package(22, "6351 South 900 East", "Sacramento", "CA","84121","EOD",2, "N/A")
package23 = Package.Package(23, "5100 South 2700 West", "Sacramento", "CA","84118","EOD",5, "N/A")
package24 = Package.Package(24, "5025 State St", "Sacramento", "CA","84107","EOD",7, "N/A")
package25 = Package.Package(25, "5383 South 900 East #104", "Sacramento", "CA","84117","10:30 AM",7,"Delayed on flight---will not arrive to depot until 9:05 am")
package26 = Package.Package(26, "5383 South 900 East #104", "Sacramento", "CA","84117","EOD",25, "N/A")
package27 = Package.Package(27, "1060 Dalton Ave S", "Sacramento", "CA","84104","EOD",5, "N/A")
package28 = Package.Package(28, "2835 Main St", "Sacramento", "CA","84115","EOD",7,"Delayed on flight---will not arrive to depot until 9:05 am")
package29 = Package.Package(29, "1330 2100 S", "Sacramento", "CA","84106","10:30 AM",2, "N/A")
package30 = Package.Package(30, "300 State St", "Sacramento", "CA","84103","10:30 AM",1, "N/A")
package31 = Package.Package(31, "3365 S 900 W", "Sacramento", "CA","84119","10:30 AM",1, "N/A")
package32 = Package.Package(32, "3365 S 900 W", "Sacramento", "CA","84119","EOD",1,"Delayed on flight---will not arrive to depot until 9:05 am")
package33 = Package.Package(33, "2530 S 500 E", "Sacramento", "CA","84106","EOD",1, "N/A")
package34 = Package.Package(34, "4580 S 2300 E", "Sacramento", "CA","84117","10:30 AM",2, "N/A")
package35 = Package.Package(35, "1060 Dalton Ave S", "Sacramento", "CA","84104","EOD",88, "N/A")
package36 = Package.Package(36, "2300 Parkway Blvd", "Sacramento", "CA","84119","EOD",88,"Can only be on truck 2")
package37 = Package.Package(37, "410 S State St", "Sacramento", "CA","84111","10:30 AM",2, "N/A")
package38 = Package.Package(38, "410 S State St", "Sacramento", "CA","84111","EOD",9,"Can only be on truck 2")
package39 = Package.Package(39, "2010 W 500 S", "Sacramento", "CA","84104","EOD",9, "N/A")
package40 = Package.Package(40, "380 W 2880 S", "Sacramento", "CA","84115","10:30 AM",45, "N/A")

#Created an instance of the Chaning Hash Table and inserted each package object into the Chaining Hash Table
#Space Complexity Big O(n)
packageHashtable = ChainingHashTable()
packageHashtable.insert(1, package1)
packageHashtable.insert(2, package2)
packageHashtable.insert(3, package3)
packageHashtable.insert(4, package4)
packageHashtable.insert(5, package5)
packageHashtable.insert(6, package6)
packageHashtable.insert(7, package7)
packageHashtable.insert(8, package8)
packageHashtable.insert(9, package9)
packageHashtable.insert(10, package10)
packageHashtable.insert(11, package11)
packageHashtable.insert(12, package12)
packageHashtable.insert(13, package13)
packageHashtable.insert(14, package14)
packageHashtable.insert(15, package15)
packageHashtable.insert(16, package16)
packageHashtable.insert(17, package17)
packageHashtable.insert(18, package18)
packageHashtable.insert(19, package19)
packageHashtable.insert(20, package20)
packageHashtable.insert(21, package21)
packageHashtable.insert(22, package22)
packageHashtable.insert(23, package23)
packageHashtable.insert(24, package24)
packageHashtable.insert(25, package25)
packageHashtable.insert(26, package26)
packageHashtable.insert(27, package27)
packageHashtable.insert(28, package28)
packageHashtable.insert(29, package29)
packageHashtable.insert(30, package30)
packageHashtable.insert(31, package31)
packageHashtable.insert(32, package32)
packageHashtable.insert(33, package33)
packageHashtable.insert(34, package34)
packageHashtable.insert(35, package35)
packageHashtable.insert(36, package36)
packageHashtable.insert(37, package37)
packageHashtable.insert(38, package38)
packageHashtable.insert(39, package39)
packageHashtable.insert(40, package40)


#Created a 2d array for the ditance between two locations
#Space Complexity: Big O (n^2)
distanceArray = [
[0.0],
[7.2,0.0],
[3.8,7.1,0.0],
[11.0,6.4,9.2,0.0],
[2.2,6.0,4.4,5.6,0.0],
[3.5,4.8,2.8,6.9,1.9,0.0],
[10.9,1.6,8.6,8.6,7.9,6.3,0.0],
[8.6,2.8,6.3,4.0,5.1,4.3,4.0,0.0],
[7.6,4.8,5.3,11.1,7.5,4.5,4.2,7.7,0.0],
[2.8,6.3,1.6,7.3,2.6,1.5,8.0,9.3,4.8,0.0],
[6.4,7.3,10.4,1.0,6.5,8.7,8.6,4.6,11.9,9.4,0.0],
[3.2,5.3,3.0,6.4,1.5,0.8,6.9,4.8,4.7,1.1,7.3,0.0],
[7.6,4.8,5.3,11.1,7.5,4.5,4.2,7.7,0.6,5.1,12.0,4.7,0.0],
[5.2,3.0,6.5,3.9,3.2,3.9,4.2,1.6,7.6,4.6,4.9,3.5,7.3,0.0],
[4.4,4.6,5.6,4.3,2.4,3.0,8.0,3.3,7.8,3.7,5.2,2.6,7.8,1.3,0.0],
[3.7,4.5,5.8,4.4,2.7,3.8,5.8,3.4,6.6,4.0,5.4,2.9,6.6,1.5,0.6,0.0],
[7.6,7.4,5.7,7.2,1.4,5.7,7.2,3.1,7.2,6.7,8.1,6.3,7.2,4.0,6.4,5.6,0.0],
[2.0,6.0,4.1,5.3,0.5,1.9,7.7,5.1,5.9,2.3,6.2,1.2,5.9,3.2,2.4,1.6,7.1,0.0],
[3.6,5.0,3.6,6.0,1.7,1.1,6.6,4.6,5.4,1.8,6.9,1.0,5.4,3.0,2.2,1.7,6.1,1.6,0.0],
[6.5,4.8,4.3,10.6,6.5,3.5,3.2,6.7,1.0,4.1,11.5,3.7,1.0,6.9,6.8,6.4,7.2,4.9,4.4,0.0],
[1.9,9.5,3.3,5.9,3.2,4.9,11.2,8.1,8.5,3.8,6.9,4.1,8.5,6.2,5.3,4.9,10.6,3.0,4.6,7.5,0.0],
[3.4,10.9,5.0,7.4,5.2,6.9,12.7,10.4,10.3,5.8,8.3,6.2,10.3,8.2,7.4,6.9,12.0,5.0,6.6,9.3,2.0,0.0],
[2.4,8.3,6.1,4.7,2.5,4.2,10.0,7.8,7.8,4.3,4.1,3.4,7.8,5.5,4.6,4.2,9.4,2.3,3.9,6.8,2.9,4.4,0.0],
[6.4,6.9,9.7,0.6,6.0,9.0,8.2,4.2,11.5,7.8,0.4,6.9,11.5,4.4,4.8,5.6,7.5,5.5,6.5,11.4,6.4,7.9,4.5,0.0],
[2.4,10.0,6.1,6.4,4.2,5.9,11.7,9.5,9.5,4.8,4.9,5.2,9.5,7.2,6.3,5.9,11.1,4.0,5.6,8.5,2.8,3.4,1.7,5.4,0.0],
[5.0,4.4,2.8,10.1,5.4,3.5,5.1,6.2,2.8,3.2,11.0,3.7,2.8,6.4,6.5,5.7,6.2,5.1,4.3,1.8,6.0,7.9,6.8,10.6,7.0,0.0],
[3.6,13.0,7.4,10.1,5.5,7.2,14.2,10.7,14.1,6.0,6.8,6.4,14.1,10.5,8.8,8.4,13.6,5.2,6.9,13.1,4.1,4.7,3.1,7.8,1.3,8.3,0.0]
]

#This function takes an address and outputs an index to be used by another function.
#Run-time Complexity Big O(n)
def addressLookUp(address):
    global index
    if address == "hub":
        index = 0
    elif address ==  "1060 Dalton Ave S":
        index = 1
    elif address == "1330 2100 S":
        index = 2
    elif address ==  "1488 4800 S":
        index = 3
    elif address == "177 W Price Ave":
        index = 4
    elif address == "195 W Oakland Ave":
        index = 5
    elif address == "2010 W 500 S":
        index = 6
    elif address == "2300 Parkway Blvd":
        index = 7
    elif address == "233 Canyon Rd":
        index = 8
    elif address == "2530 S 500 E":
        index = 9
    elif address == "2600 Taylorsville Blvd":
        index = 10
    elif address == "2835 Main St":
        index = 11
    elif address == "300 State St":
        index = 12
    elif address == "3060 Lester St":
        index = 13
    elif address == "3148 S 1100 W":
        index = 14
    elif address == "3365 S 900 W":
        index = 15
    elif address == "3575 W Valley Central Station bus Loop":
        index = 16
    elif address == "3595 Main St":
        index = 17
    elif address == "380 W 2880 S":
        index = 18
    elif address == "410 S State St":
        index = 19
    elif address == "4300 S 1300 E":
        index = 20
    elif address == "4580 S 2300 E":
        index = 21
    elif address == "5025 State St":
        index = 22
    elif address == "5100 South 2700 West":
        index = 23
    elif address == "5383 South 900 East #104":
        index = 24
    elif address == "600 E 900 South":
        index = 25
    elif address == "6351 South 900 East":
        index = 26
    return index

    #This function takes two addresses, a start location and a destination location, and outputs the distance between the two.
    # Run-time Complexity Big O(1)
def distanceLookUp(address1, address2):
   a1 = addressLookUp(address1)
   a2 = addressLookUp(address2)
   if a2 > a1:
       tempA1 = a1
       tempA2 = a2
       a1 = tempA2
       a2 = tempA1
   distance = distanceArray[a1][a2]
   return distance

#These list represent manually loaded packages into trucks
#Space Complexity of each truck creation Big O(1)
truck1 = [13,14,15,16,19,20,39,34,21,7,29,27,35,36,2,33]
truck2 = [3,18, 24,1,22,40,31,10,12,17,4,37,5,38,11,23]
truck3 = [6,25,32,26,28,30,9,8]


#Big O(n^2) Nearest Neighbor Algorithim. This function takes as an input the packages inside of a truck.
#The first thing the function does is checks to see if there are packages inside of the truck. While
#packages still remain in the truck, it compares the distance from the current location of the truck
#and the distance between every other package destination. The algorithim chooses the package that is
#shortest distance from the current location as the next drop off. It then calculates the the distance it takes to get
#to the next location and adds it to the total distance traveled. It also timestamps the time the package is delivered.
#the package and adds that time to the total time traveled. After this, the packakage is removed from the truck list.
#When there are no longer any packages inside of the truck the truck adds the distance it takes to get back to the hub
#and outputs the total distance travel.
def truckDeliverPackages(truck):
    packageID = None
    totalTravelDistance = 0
    currentTruckLocation = "hub"
    deliveryTime = 8.0
    if truck == truck3:
        deliveryTime = 9.4
    while len(truck) > 0:
        minValue = 500
        minPackageID = None
        for packageID in truck:
             package = packageHashtable.search(packageID)
             packageAddress = package.address
             travelDistance = distanceLookUp(currentTruckLocation, packageAddress)
             if minValue > travelDistance:
                minValue = travelDistance
                minPackageID = packageID
        tempPackage = packageHashtable.search(minPackageID)
        currentTruckLocation = tempPackage.address
        totalTravelDistance += minValue
        deliveryTime += minValue / 18
        tempPackage.deliveryTime = deliveryTime
        truck.remove(minPackageID)
    travelDistance = distanceLookUp(currentTruckLocation, "hub")
    totalTravelDistance += travelDistance
    return totalTravelDistance
print("Total distance traveled in miles:")
print(truckDeliverPackages(truck1)+truckDeliverPackages(truck2)+truckDeliverPackages(truck3))

#This is a call by refrence of the truck delivery function using the truck objects in the parameters.
truckDeliverPackages(truck1)
truckDeliverPackages(truck2)
truckDeliverPackages(truck3)

#This is the command line interface that request a time input from the user to check package status.
timeToCheck = input("Please input desired time to check(using a number format; for example 9:30am"
                    " would be 9.5; 2:30pm would be 14.5):")

#Run-time Complexity Big O(n) This for-loop looks through all of the packages and outputs the current status to the display
# based on the input time that the user gives.
#(“convert number to time python” Code Answer”, 2022)
for i in range(1, 41):
    package = packageHashtable.search(i)
    if i == 13 or i == 14 or i == 16 or i == 19 or i == 20 or i == 39 or i == 34 or i == 21 or i == 7 or i == 29 or i == 27 or i == 35 or i == 36 or i == 2 or i == 33 or i == 15:
        print("Truck 1 Package:")
        print(packageHashtable.search(i))
    if i == 3 or i == 18 or i == 24 or i == 1 or i == 22 or i == 40 or i == 31 or i == 10 or i == 12 or i == 17 or i == 4 or i == 37 or i == 5 or i == 38 or i == 11 or i == 23:
        print("Truck 2 Package:")
        print(packageHashtable.search(i))
    if i == 6 or i == 25 or i == 32 or i == 26 or i == 28 or i == 30 or i == 9 or i == 8:
        print("Truck 3 Package:")
        print(packageHashtable.search(i))
    if package.deliveryTime < float(timeToCheck):
        hrs = int(package.deliveryTime)
        mins = (package.deliveryTime * 60) % 60
        print("delivered: " + "%d:%02d" % (hrs, mins) + " a.m.")
    elif (i == 6 or i == 25 or i == 32 or i == 26 or i == 28 or i == 30 or i == 9 or i == 8) and float(timeToCheck) < 9.63:
        print("at the hub")
    else:
        print("en route")
        truck1 = [13, 14, 15, 16, 19, 20, 39, 34, 21, 7, 29, 27, 35, 36, 2, 33]
        truck2 = [3, 18, 24, 1, 22, 40, 31, 10, 12, 17, 4, 37, 5, 38, 11, 23]
        truck3 = [6, 25, 32, 26, 28, 30, 9, 8]
