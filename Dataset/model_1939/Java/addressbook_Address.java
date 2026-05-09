





import java.util.List;
import java.util.ArrayList;

public class addressbook_Address  {

    private String city;
    private String street;
    private String zip;
    private String type;





    private addressbook_Country addressbook_country;


    public addressbook_Address(
        String city,        String street,        String zip,        String type    ) {
        this.city = city;
        this.street = street;
        this.zip = zip;
        this.type = type;
    }


    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }
    public String getStreet() {
        return street;
    }

    public void setStreet(String street) {
        this.street = street;
    }
    public String getZip() {
        return zip;
    }

    public void setZip(String zip) {
        this.zip = zip;
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

}