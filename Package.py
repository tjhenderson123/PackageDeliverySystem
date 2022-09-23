class Package:

    def __init__(self, iD, address, city, state, zip, deliveryDeadline, massKilo, specialNotes):
        self.iD = iD
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deliveryDeadlline = deliveryDeadline
        self.massKilo = massKilo
        self.specialNotes = specialNotes
        self.deliveryTime = None

    # overwrite to print parameters.
    #deleted placeholder that shows deliverytime
    #used from https://wgu.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=eee77a88-4de8-4d42-a3c3-ac8000ece256
    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s. %s" % (self.iD, self.address, self.city, self.state,
                                                   self.zip, self.deliveryDeadlline, self.massKilo,
                                                   self.specialNotes)
