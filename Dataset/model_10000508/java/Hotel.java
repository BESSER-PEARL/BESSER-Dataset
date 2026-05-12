





import java.util.List;
import java.util.ArrayList;

public class Hotel  {

    private int coordinates;
    private int zip;
    private String name;
    private String website;
    private String city;
    private int phoneNumber;
    private String street;



    public Hotel(
        int coordinates,        int zip,        String name,        String website,        String city,        int phoneNumber,        String street    ) {
        this.coordinates = coordinates;
        this.zip = zip;
        this.name = name;
        this.website = website;
        this.city = city;
        this.phoneNumber = phoneNumber;
        this.street = street;
    }


    public int getCoordinates() {
        return coordinates;
    }

    public void setCoordinates(int coordinates) {
        this.coordinates = coordinates;
    }
    public int getZip() {
        return zip;
    }

    public void setZip(int zip) {
        this.zip = zip;
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
    public String getStreet() {
        return street;
    }

    public void setStreet(String street) {
        this.street = street;
    }


}