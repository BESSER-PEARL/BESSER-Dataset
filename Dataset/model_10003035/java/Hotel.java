





import java.util.List;
import java.util.ArrayList;

public class Hotel  {

    private int coordinates;
    private String website;
    private int phoneNumber;
    private String city;
    private int zip;
    private String name;
    private String street;



    public Hotel(
        int coordinates,        String website,        int phoneNumber,        String city,        int zip,        String name,        String street    ) {
        this.coordinates = coordinates;
        this.website = website;
        this.phoneNumber = phoneNumber;
        this.city = city;
        this.zip = zip;
        this.name = name;
        this.street = street;
    }


    public int getCoordinates() {
        return coordinates;
    }

    public void setCoordinates(int coordinates) {
        this.coordinates = coordinates;
    }
    public String getWebsite() {
        return website;
    }

    public void setWebsite(String website) {
        this.website = website;
    }
    public int getPhonenumber() {
        return phoneNumber;
    }

    public void setPhonenumber(int phoneNumber) {
        this.phoneNumber = phoneNumber;
    }
    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
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
    public String getStreet() {
        return street;
    }

    public void setStreet(String street) {
        this.street = street;
    }


}