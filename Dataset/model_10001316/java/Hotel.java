





import java.util.List;
import java.util.ArrayList;

public class Hotel  {

    private String city;
    private String street;
    private int zip;
    private String website;
    private int coordinates;
    private String name;
    private int phoneNumber;



    public Hotel(
        String city,        String street,        int zip,        String website,        int coordinates,        String name,        int phoneNumber    ) {
        this.city = city;
        this.street = street;
        this.zip = zip;
        this.website = website;
        this.coordinates = coordinates;
        this.name = name;
        this.phoneNumber = phoneNumber;
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
    public int getPhonenumber() {
        return phoneNumber;
    }

    public void setPhonenumber(int phoneNumber) {
        this.phoneNumber = phoneNumber;
    }


}