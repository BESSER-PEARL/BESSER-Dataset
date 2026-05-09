





import java.util.List;
import java.util.ArrayList;

public class contacts_UoD  {






    private List<contacts_AddressBook> contacts_addressbooks;


    public contacts_UoD(
    ) {
        this.contacts_addressbooks = new ArrayList<>();
    }

    public contacts_UoD(
        ArrayList<contacts_AddressBook> contacts_addressbooks    ) {
        this.contacts_addressbooks = contacts_addressbooks;
    }


    public List<contacts_AddressBook> getContacts_addressbooks() {
        return contacts_addressbooks;
    }

    public void addContacts_addressbook(Contacts_addressbook contacts_addressbook) {
        this.contacts_addressbooks.add(contacts_addressbook);
    }

}