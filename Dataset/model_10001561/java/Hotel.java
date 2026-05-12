





import java.util.List;
import java.util.ArrayList;

public class Hotel  {

    private int coordinates;
    private String city;
    private String name;
    private int zip;
    private String street;
    private int phoneNumber;
    private String website;



    public Hotel(
        int coordinates,        String city,        String name,        int zip,        String street,        int phoneNumber,        String website    ) {
        this.coordinates = coordinates;
        this.city = city;
        this.name = name;
        this.zip = zip;
        this.street = street;
        this.phoneNumber = phoneNumber;
        this.website = website;
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
    public int getZip() {
        return zip;
    }

    public void setZip(int zip) {
        this.zip = zip;
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
    public String getWebsite() {
        return website;
    }

    public void setWebsite(String website) {
        this.website = website;
    }


}