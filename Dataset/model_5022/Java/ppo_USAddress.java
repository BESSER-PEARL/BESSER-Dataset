





import java.util.List;
import java.util.ArrayList;

public class ppo_USAddress  {

    private String name;
    private String state;
    private String country;
    private String city;
    private int zip;
    private String street;



    public ppo_USAddress(
        String name,        String state,        String country,        String city,        int zip,        String street    ) {
        this.name = name;
        this.state = state;
        this.country = country;
        this.city = city;
        this.zip = zip;
        this.street = street;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }
    public String getCountry() {
        return country;
    }

    public void setCountry(String country) {
        this.country = country;
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
    public String getStreet() {
        return street;
    }

    public void setStreet(String street) {
        this.street = street;
    }


}