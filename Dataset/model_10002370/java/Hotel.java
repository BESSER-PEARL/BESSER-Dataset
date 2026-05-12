





import java.util.List;
import java.util.ArrayList;

public class Hotel  {

    private String name;
    private String website;
    private String city;
    private String street;
    private int phoneNumber;
    private int coordinates;
    private int zip;



    public Hotel(
        String name,        String website,        String city,        String street,        int phoneNumber,        int coordinates,        int zip    ) {
        this.name = name;
        this.website = website;
        this.city = city;
        this.street = street;
        this.phoneNumber = phoneNumber;
        this.coordinates = coordinates;
        this.zip = zip;
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
    public int getPhonenumber() {
        return phoneNumber;
    }

    public void setPhonenumber(int phoneNumber) {
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


}