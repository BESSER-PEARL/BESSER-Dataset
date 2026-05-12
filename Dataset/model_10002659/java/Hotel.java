





import java.util.List;
import java.util.ArrayList;

public class Hotel  {

    private int coordinates;
    private int zip;
    private String city;
    private String street;
    private String name;
    private String website;
    private int phoneNumber;



    public Hotel(
        int coordinates,        int zip,        String city,        String street,        String name,        String website,        int phoneNumber    ) {
        this.coordinates = coordinates;
        this.zip = zip;
        this.city = city;
        this.street = street;
        this.name = name;
        this.website = website;
        this.phoneNumber = phoneNumber;
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
    public int getPhonenumber() {
        return phoneNumber;
    }

    public void setPhonenumber(int phoneNumber) {
        this.phoneNumber = phoneNumber;
    }


}