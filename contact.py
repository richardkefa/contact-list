import pyperclip

class Contact:
  """
  class that generates new instance of contacts
  """
  pass

  def __init__(self,first_name,last_name,phone_number,email):

    """

    __init__method that help us define properties for our objects.
      
      Args:
          first_name: New contact first name.
          last_name: New  contact last name.
          number: New contact phone address.
          email : New contact email address.

    """

    #docstring rmoved for simplicity

    self.first_name = first_name
    self.last_name = last_name
    self.phone_number = phone_number
    self.email = email

  contact_list = [] #Empty contact list
    #Init method up here
  def save_contact(self):
        '''
        save_contact method saves contact object into contact_list
        '''
        Contact.contact_list.append(self)

  def delete_contact(self):
    '''
    delete_contact method deletes a saved contact from the contact list
    '''
    Contact.contact_list.remove(self)

  @classmethod 
  def find_by_number(cls,number):
    '''
    method that takes in a number and rturns a contact that matches that number.

    Args:
     number: Phone number to search for 
    returns :
      Contact of person that matches the number
    '''
    for contact in cls.contact_list:
      if contact.phone_number == number:
        return contact

  @classmethod
  def contact_exist(cls,number):
    for contact in cls.contact_list:
      if contact.phone_number==number:
        return True
    return False

  @classmethod
  def display_contacts(cls):
    return cls.contact_list

  @classmethod
  def copy_email(cls,number):
    contact_found = Contact.find_by_number(number)
    pyperclip.copy(contact_found.email)