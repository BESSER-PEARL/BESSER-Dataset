





import java.util.List;
import java.util.ArrayList;

public class addressbook_Person  {

    private String firstname;
    private String lastname;





    private addressbook_Address addressbook_address;




    private addressbook_AddressBook addressbook_addressbook;




    private List<addressbook_Address> addressbook_addresss;




    private addressbook_AddressBook addressbook_addressbook;


    public addressbook_Person(
        String firstname,        String lastname    ) {
        this.firstname = firstname;
        this.lastname = lastname;
        this.addressbook_addresss = new ArrayList<>();
    }

    public addressbook_Person(
        String firstname,        String lastname        ArrayList<addressbook_Address> addressbook_addresss    ) {
        this.firstname = firstname;
        this.lastname = lastname;
        this.addressbook_addresss = addressbook_addresss;
    }

    public String getFirstname() {
        return firstname;
    }

    public void setFirstname(String firstname) {
        this.firstname = firstname;
    }
    public String getLastname() {
        return lastname;
    }

    public void setLastname(String lastname) {
        this.lastname = lastname;
    }

    public addressbook_Address getAddressbook_address() {
        return addressbook_address;
    }

    public void setAddressbook_address(addressbook_Address addressbook_address) {
        this.addressbook_address = addressbook_address;
    }
    public addressbook_AddressBook getAddressbook_addressbook() {
        return addressbook_addressbook;
    }

    public void setAddressbook_addressbook(addressbook_AddressBook addressbook_addressbook) {
        this.addressbook_addressbook = addressbook_addressbook;
    }
    public List<addressbook_Address> getAddressbook_addresss() {
        return addressbook_addresss;
    }

    public void addAddressbook_address(Addressbook_address addressbook_address) {
        this.addressbook_addresss.add(addressbook_address);
    }
    public addressbook_AddressBook getAddressbook_addressbook() {
        return addressbook_addressbook;
    }

    public void setAddressbook_addressbook(addressbook_AddressBook addressbook_addressbook) {
        this.addressbook_addressbook = addressbook_addressbook;
    }

}