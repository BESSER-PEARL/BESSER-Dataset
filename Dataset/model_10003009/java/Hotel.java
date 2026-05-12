





import java.util.List;
import java.util.ArrayList;

public class Hotel  {

    private String city;
    private String name;
    private String website;
    private String street;
    private int phoneNumber;
    private int zip;
    private int coordinates;



    public Hotel(
        String city,        String name,        String website,        String street,        int phoneNumber,        int zip,        int coordinates    ) {
        this.city = city;
        this.name = name;
        this.website = website;
        this.street = street;
        this.phoneNumber = phoneNumber;
        this.zip = zip;
        this.coordinates = coordinates;
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
    public int getCoordinates() {
        return coordinates;
    }

    public void setCoordinates(int coordinates) {
        this.coordinates = coordinates;
    }


}