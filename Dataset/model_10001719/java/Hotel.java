





import java.util.List;
import java.util.ArrayList;

public class Hotel  {

    private String name;
    private int zip;
    private int coordinates;
    private int phoneNumber;
    private String website;
    private String street;
    private String city;



    public Hotel(
        String name,        int zip,        int coordinates,        int phoneNumber,        String website,        String street,        String city    ) {
        this.name = name;
        this.zip = zip;
        this.coordinates = coordinates;
        this.phoneNumber = phoneNumber;
        this.website = website;
        this.street = street;
        this.city = city;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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
    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }


}