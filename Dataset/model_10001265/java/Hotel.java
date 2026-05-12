





import java.util.List;
import java.util.ArrayList;

public class Hotel  {

    private int phoneNumber;
    private String website;
    private String street;
    private int coordinates;
    private String city;
    private int zip;
    private String name;



    public Hotel(
        int phoneNumber,        String website,        String street,        int coordinates,        String city,        int zip,        String name    ) {
        this.phoneNumber = phoneNumber;
        this.website = website;
        this.street = street;
        this.coordinates = coordinates;
        this.city = city;
        this.zip = zip;
        this.name = name;
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


}