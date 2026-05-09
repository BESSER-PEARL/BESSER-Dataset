





import java.util.List;
import java.util.ArrayList;

public class addressbook_BookVersion  {

    private int id;





    private addressbook_AddressBook addressbook_addressbook;




    private addressbook_Repository addressbook_repository;


    public addressbook_BookVersion(
        int id    ) {
        this.id = id;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public addressbook_AddressBook getAddressbook_addressbook() {
        return addressbook_addressbook;
    }

    public void setAddressbook_addressbook(addressbook_AddressBook addressbook_addressbook) {
        this.addressbook_addressbook = addressbook_addressbook;
    }
    public addressbook_Repository getAddressbook_repository() {
        return addressbook_repository;
    }

    public void setAddressbook_repository(addressbook_Repository addressbook_repository) {
        this.addressbook_repository = addressbook_repository;
    }

}