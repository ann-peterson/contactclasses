class Contact(object):
    def __init__ (self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.mobile_number = ""
        self.email = ""

    def send_text(self,text):
        print "To: %s - %s" % (self.mobile_number, text)

    def display_name(self):
        return "Name: %s %s" % (self.first_name, self.last_name)



contact_list = []

def main():
    contact_carly = Contact("Carly","Fujiyoshi")
    contact_ann = Contact("Ann","Peterson")
    contact_jane = Contact("Jane","Doe")
    contact_list.append(contact_carly)
    contact_list.append(contact_ann)
    contact_list.append(contact_jane)
    for contact in contact_list:
        print contact.display_name()


if __name__ == "__main__":
    main()

# ann = Contact("Ann","Peterson")

# ann.email = "email@email.com"
# ann.mobile_number = "555-5555"
# ann.send_text("What's up?")
# print ann.display_name()