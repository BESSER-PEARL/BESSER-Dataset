





import java.util.List;
import java.util.ArrayList;

public class addressbook_Address  {

    private String zip;
    private String street;
    private String city;
    private String type;





    private addressbook_Country addressbook_country;




    private addressbook_Person addressbook_person;




    private addressbook_Person addressbook_person;


    public addressbook_Address(
        String zip,        String street,        String city,        String type    ) {
        this.zip = zip;
        this.street = street;
        this.city = city;
        this.type = type;
    }


    public String getZip() {
        return zip;
    }

    public void setZip(String zip) {
        this.zip = zip;
    }
    public String getStreet() {
        return street;
    }

    public void setStreet(String street) {
        this.street = street;
    }
    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public addressbook_Country getAddressbook_country() {
        return addressbook_country;
    }

    public void setAddressbook_country(addressbook_Country addressbook_country) {
        this.addressbook_country = addressbook_country;
    }
    public addressbook_Person getAddressbook_person() {
        return addressbook_person;
    }

    public void setAddressbook_person(addressbook_Person addressbook_person) {
        this.addressbook_person = addressbook_person;
    }
    public addressbook_Person getAddressbook_person() {
        return addressbook_person;
    }

    public void setAddressbook_person(addressbook_Person addressbook_person) {
        this.addressbook_person = addressbook_person;
    }

}