





import java.util.List;
import java.util.ArrayList;

public class Hotel  {

    private String website;
    private String street;
    private String name;
    private int coordinates;
    private int zip;
    private int phoneNumber;
    private String city;



    public Hotel(
        String website,        String street,        String name,        int coordinates,        int zip,        int phoneNumber,        String city    ) {
        this.website = website;
        this.street = street;
        this.name = name;
        this.coordinates = coordinates;
        this.zip = zip;
        this.phoneNumber = phoneNumber;
        this.city = city;
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


}