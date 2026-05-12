





import java.util.List;
import java.util.ArrayList;

public class Hotel  {

    private String city;
    private int zip;
    private int coordinates;
    private int phoneNumber;
    private String street;
    private String name;
    private String website;



    public Hotel(
        String city,        int zip,        int coordinates,        int phoneNumber,        String street,        String name,        String website    ) {
        this.city = city;
        this.zip = zip;
        this.coordinates = coordinates;
        this.phoneNumber = phoneNumber;
        this.street = street;
        this.name = name;
        this.website = website;
    }


    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
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


}