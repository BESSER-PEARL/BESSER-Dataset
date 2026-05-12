





import java.util.List;
import java.util.ArrayList;

public class Hotel  {

    private int coordinates;
    private String street;
    private int zip;
    private int phoneNumber;
    private String website;
    private String name;
    private String city;



    public Hotel(
        int coordinates,        String street,        int zip,        int phoneNumber,        String website,        String name,        String city    ) {
        this.coordinates = coordinates;
        this.street = street;
        this.zip = zip;
        this.phoneNumber = phoneNumber;
        this.website = website;
        this.name = name;
        this.city = city;
    }


    public int getCoordinates() {
        return coordinates;
    }

    public void setCoordinates(int coordinates) {
        this.coordinates = coordinates;
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
    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }


}