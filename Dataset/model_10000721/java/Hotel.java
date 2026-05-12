





import java.util.List;
import java.util.ArrayList;

public class Hotel  {

    private String city;
    private int phoneNumber;
    private String website;
    private String name;
    private int coordinates;
    private int zip;
    private String street;



    public Hotel(
        String city,        int phoneNumber,        String website,        String name,        int coordinates,        int zip,        String street    ) {
        this.city = city;
        this.phoneNumber = phoneNumber;
        this.website = website;
        this.name = name;
        this.coordinates = coordinates;
        this.zip = zip;
        this.street = street;
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
    public String getWebsite() {
        return website;
    }

    public void setWebsite(String website) {
        this.website = website;
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
    public int getZip() {
        return zip;
    }

    public void setZip(int zip) {
        this.zip = zip;
    }
    public String getStreet() {
        return street;
    }

    public void setStreet(String street) {
        this.street = street;
    }


}