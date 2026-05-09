





import java.util.List;
import java.util.ArrayList;

public class contacts_AddressBook  {






    private List<contacts_Contact> contacts_contacts;


    public contacts_AddressBook(
    ) {
        this.contacts_contacts = new ArrayList<>();
    }

    public contacts_AddressBook(
        ArrayList<contacts_Contact> contacts_contacts    ) {
        this.contacts_contacts = contacts_contacts;
    }


    public List<contacts_Contact> getContacts_contacts() {
        return contacts_contacts;
    }

    public void addContacts_contact(Contacts_contact contacts_contact) {
        this.contacts_contacts.add(contacts_contact);
    }

}