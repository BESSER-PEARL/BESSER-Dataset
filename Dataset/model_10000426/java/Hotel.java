





import java.util.List;
import java.util.ArrayList;

public class Hotel  {

    private String website;
    private String street;
    private int zip;
    private String city;
    private int phoneNumber;
    private String name;
    private int coordinates;



    public Hotel(
        String website,        String street,        int zip,        String city,        int phoneNumber,        String name,        int coordinates    ) {
        this.website = website;
        this.street = street;
        this.zip = zip;
        this.city = city;
        this.phoneNumber = phoneNumber;
        this.name = name;
        this.coordinates = coordinates;
    }


    public String getWebsite() {
        return website;
    }

    public void setWebsite(String website) {
        this.website = website;
    }
    public String getStreet() {
        return street;
    }

    public void setStreet(String street) {
        this.street = street;
    }
    public int getZip() {
        return zip;
    }

    public void setZip(int zip) {
        this.zip = zip;
    }
    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }
    public int getPhonenumber() {
        return phoneNumber;
    }

    public void setPhonenumber(int phoneNumber) {
        this.phoneNumber = phoneNumber;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getCoordinates() {
        return coordinates;
    }

    public void setCoordinates(int coordinates) {
        this.coordinates = coordinates;
    }


}