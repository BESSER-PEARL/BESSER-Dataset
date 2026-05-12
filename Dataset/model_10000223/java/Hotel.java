





import java.util.List;
import java.util.ArrayList;

public class Hotel  {

    private int phoneNumber;
    private String street;
    private String website;
    private String name;
    private int coordinates;
    private String city;
    private int zip;



    public Hotel(
        int phoneNumber,        String street,        String website,        String name,        int coordinates,        String city,        int zip    ) {
        this.phoneNumber = phoneNumber;
        this.street = street;
        this.website = website;
        this.name = name;
        this.coordinates = coordinates;
        this.city = city;
        this.zip = zip;
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
    public int getZip() {
        return zip;
    }

    public void setZip(int zip) {
        this.zip = zip;
    }


}