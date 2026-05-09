





import java.util.List;
import java.util.ArrayList;

public class addressbook_Address  {

    private String Street;
    private String HouseNr;
    private String City;





    private addressbook_Contact addressbook_contact;


    public addressbook_Address(
        String Street,        String HouseNr,        String City    ) {
        this.Street = Street;
        this.HouseNr = HouseNr;
        this.City = City;
    }


    public String getStreet() {
        return Street;
    }

    public void setStreet(String Street) {
        this.Street = Street;
    }
    public String getHousenr() {
        return HouseNr;
    }

    public void setHousenr(String HouseNr) {
        this.HouseNr = HouseNr;
    }
    public String getCity() {
        return City;
    }

    public void setCity(String City) {
        this.City = City;
    }

    public addressbook_Contact getAddressbook_contact() {
        return addressbook_contact;
    }

    public void setAddressbook_contact(addressbook_Contact addressbook_contact) {
        this.addressbook_contact = addressbook_contact;
    }

}