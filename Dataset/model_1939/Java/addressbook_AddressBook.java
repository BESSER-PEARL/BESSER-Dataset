





import java.util.List;
import java.util.ArrayList;

public class addressbook_AddressBook  {






    private List<addressbook_Country> addressbook_countrys;




    private addressbook_Country addressbook_country;


    public addressbook_AddressBook(
    ) {
        this.addressbook_countrys = new ArrayList<>();
    }

    public addressbook_AddressBook(
        ArrayList<addressbook_Country> addressbook_countrys    ) {
        this.addressbook_countrys = addressbook_countrys;
    }


    public List<addressbook_Country> getAddressbook_countrys() {
        return addressbook_countrys;
    }

    public void addAddressbook_country(Addressbook_country addressbook_country) {
        this.addressbook_countrys.add(addressbook_country);
    }
    public addressbook_Country getAddressbook_country() {
        return addressbook_country;
    }

    public void setAddressbook_country(addressbook_Country addressbook_country) {
        this.addressbook_country = addressbook_country;
    }

}