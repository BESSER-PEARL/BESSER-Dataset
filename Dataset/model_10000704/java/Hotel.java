





import java.util.List;
import java.util.ArrayList;

public class Hotel  {

    private String street;
    private String website;
    private String city;
    private String name;
    private int phoneNumber;
    private int zip;



    public Hotel(
        String street,        String website,        String city,        String name,        int phoneNumber,        int zip    ) {
        this.street = street;
        this.website = website;
        this.city = city;
        this.name = name;
        this.phoneNumber = phoneNumber;
        this.zip = zip;
    }


    public String getStreet() {
        return street;
    }

    public void setStreet(String street) {
        this.street = street;
    }
    public String getWebsite() {
        return website;
    }

    public void setWebsite(String website) {
        this.website = website;
    }
    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getPhonenumber() {
        return phoneNumber;
    }

    public void setPhonenumber(int phoneNumber) {
        this.phoneNumber = phoneNumber;
    }
    public int getZip() {
        return zip;
    }

    public void setZip(int zip) {
        this.zip = zip;
    }


}