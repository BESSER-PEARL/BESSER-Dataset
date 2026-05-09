





import java.util.List;
import java.util.ArrayList;

public class contacts_Address  {

    private String street;
    private String country;
    private String state;
    private String zipCode;
    private String city;





    private contacts_Contact contacts_contact;




    private contacts_Contact contacts_contact;


    public contacts_Address(
        String street,        String country,        String state,        String zipCode,        String city    ) {
        this.street = street;
        this.country = country;
        this.state = state;
        this.zipCode = zipCode;
        this.city = city;
    }


    public String getStreet() {
        return street;
    }

    public void setStreet(String street) {
        this.street = street;
    }
    public String getCountry() {
        return country;
    }

    public void setCountry(String country) {
        this.country = country;
    }
    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }
    public String getZipcode() {
        return zipCode;
    }

    public void setZipcode(String zipCode) {
        this.zipCode = zipCode;
    }
    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }

    public contacts_Contact getContacts_contact() {
        return contacts_contact;
    }

    public void setContacts_contact(contacts_Contact contacts_contact) {
        this.contacts_contact = contacts_contact;
    }
    public contacts_Contact getContacts_contact() {
        return contacts_contact;
    }

    public void setContacts_contact(contacts_Contact contacts_contact) {
        this.contacts_contact = contacts_contact;
    }

}