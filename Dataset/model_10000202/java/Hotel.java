





import java.util.List;
import java.util.ArrayList;

public class Hotel  {

    private int zip;
    private String website;
    private String city;
    private int coordinates;
    private String name;
    private String street;
    private int phoneNumber;



    public Hotel(
        int zip,        String website,        String city,        int coordinates,        String name,        String street,        int phoneNumber    ) {
        this.zip = zip;
        this.website = website;
        this.city = city;
        this.coordinates = coordinates;
        this.name = name;
        this.street = street;
        this.phoneNumber = phoneNumber;
    }


    public int getZip() {
        return zip;
    }

    public void setZip(int zip) {
        this.zip = zip;
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
    public int getCoordinates() {
        return coordinates;
    }

    public void setCoordinates(int coordinates) {
        this.coordinates = coordinates;
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
    public int getPhonenumber() {
        return phoneNumber;
    }

    public void setPhonenumber(int phoneNumber) {
        this.phoneNumber = phoneNumber;
    }


}