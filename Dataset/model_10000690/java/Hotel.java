





import java.util.List;
import java.util.ArrayList;

public class Hotel  {

    private int phoneNumber;
    private String city;
    private int coordinates;
    private String street;
    private String name;
    private int zip;
    private String website;



    public Hotel(
        int phoneNumber,        String city,        int coordinates,        String street,        String name,        int zip,        String website    ) {
        this.phoneNumber = phoneNumber;
        this.city = city;
        this.coordinates = coordinates;
        this.street = street;
        this.name = name;
        this.zip = zip;
        this.website = website;
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
    public String getWebsite() {
        return website;
    }

    public void setWebsite(String website) {
        this.website = website;
    }


}