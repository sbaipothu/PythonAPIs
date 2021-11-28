class Store:
    def __init__(self, store_object):
        self.store_name = store_object['store_name']
        self.phone = store_object['phone']
        self.email = store_object['email']
        self.street = store_object['street']
        self.city = store_object['city']
        self.state = store_object['state']
        self.zip_code = store_object['zip_code']

    def validate_store(self):
        if self.store_name in [None, '']:
            return False, "Store name cannot be empty"
        elif self.phone in [None, '']:
            return False, "Phone no. cannot be empty"
        elif self.email in [None, '']:
            return False, "Email cannot be empty"
        elif self.street in [None, '']:
            return False, "Street cannot be Empty"
        elif self.city in [None, '']:
            return False, "City cannot be Empty"
        elif self.state in [None, '']:
            return False, "State cannot be Empty"
        elif self.zip_code in [None, '']:
            return False, "ZipCode cannot be Empty"
        else:
            return True