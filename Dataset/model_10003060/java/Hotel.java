





import java.util.List;
import java.util.ArrayList;

public class Hotel  {

    private int phoneNumber;
    private String name;
    private String website;
    private int zip;
    private String city;
    private String street;
    private int coordinates;



    public Hotel(
        int phoneNumber,        String name,        String website,        int zip,        String city,        String street,        int coordinates    ) {
        this.phoneNumber = phoneNumber;
        this.name = name;
        this.website = website;
        this.zip = zip;
        this.city = city;
        this.street = street;
        this.coordinates = coordinates;
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
    public int getCoordinates() {
        return coordinates;
    }

    public void setCoordinates(int coordinates) {
        this.coordinates = coordinates;
    }


}