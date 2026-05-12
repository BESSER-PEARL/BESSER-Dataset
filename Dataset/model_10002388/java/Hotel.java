





import java.util.List;
import java.util.ArrayList;

public class Hotel  {

    private String name;
    private String street;
    private int coordinates;
    private int phoneNumber;
    private String website;
    private int zip;
    private String city;



    public Hotel(
        String name,        String street,        int coordinates,        int phoneNumber,        String website,        int zip,        String city    ) {
        this.name = name;
        this.street = street;
        this.coordinates = coordinates;
        this.phoneNumber = phoneNumber;
        this.website = website;
        this.zip = zip;
        this.city = city;
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


}