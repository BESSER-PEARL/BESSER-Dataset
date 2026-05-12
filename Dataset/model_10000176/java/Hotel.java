





import java.util.List;
import java.util.ArrayList;

public class Hotel  {

    private String street;
    private int coordinates;
    private String city;
    private String name;
    private String website;
    private int zip;
    private int phoneNumber;



    public Hotel(
        String street,        int coordinates,        String city,        String name,        String website,        int zip,        int phoneNumber    ) {
        this.street = street;
        this.coordinates = coordinates;
        this.city = city;
        this.name = name;
        this.website = website;
        this.zip = zip;
        this.phoneNumber = phoneNumber;
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
    public int getPhonenumber() {
        return phoneNumber;
    }

    public void setPhonenumber(int phoneNumber) {
        this.phoneNumber = phoneNumber;
    }


}