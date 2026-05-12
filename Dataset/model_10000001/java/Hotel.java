





import java.util.List;
import java.util.ArrayList;

public class Hotel  {

    private String street;
    private int phoneNumber;
    private String name;
    private String city;
    private String website;
    private int zip;
    private int coordinates;



    public Hotel(
        String street,        int phoneNumber,        String name,        String city,        String website,        int zip,        int coordinates    ) {
        this.street = street;
        this.phoneNumber = phoneNumber;
        this.name = name;
        this.city = city;
        this.website = website;
        this.zip = zip;
        this.coordinates = coordinates;
    }


    public String getStreet() {
        return street;
    }

    public void setStreet(String street) {
        this.street = street;
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
    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }
    public String getWebsite() {
        return website;
    }

    public void setWebsite(String website) {
        this.website = website;
    }
    public int getZip() {
        return zip;
    }

    public void setZip(int zip) {
        this.zip = zip;
    }
    public int getCoordinates() {
        return coordinates;
    }

    public void setCoordinates(int coordinates) {
        this.coordinates = coordinates;
    }


}