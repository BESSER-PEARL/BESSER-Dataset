





import java.util.List;
import java.util.ArrayList;

public class addressbook_AddressBook  {






    private List<addressbook_People> addressbook_peoples;


    public addressbook_AddressBook(
    ) {
        this.addressbook_peoples = new ArrayList<>();
    }

    public addressbook_AddressBook(
        ArrayList<addressbook_People> addressbook_peoples    ) {
        this.addressbook_peoples = addressbook_peoples;
    }


    public List<addressbook_People> getAddressbook_peoples() {
        return addressbook_peoples;
    }

    public void addAddressbook_people(Addressbook_people addressbook_people) {
        this.addressbook_peoples.add(addressbook_people);
    }

}