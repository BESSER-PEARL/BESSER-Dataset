





import java.util.List;
import java.util.ArrayList;

public class demo_model_Address  {

    private String country;
    private String city;
    private String street;
    private String state;
    private int zipcode;



    public demo_model_Address(
        String country,        String city,        String street,        String state,        int zipcode    ) {
        this.country = country;
        this.city = city;
        this.street = street;
        this.state = state;
        this.zipcode = zipcode;
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
    public String getStreet() {
        return street;
    }

    public void setStreet(String street) {
        this.street = street;
    }
    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }
    public int getZipcode() {
        return zipcode;
    }

    public void setZipcode(int zipcode) {
        this.zipcode = zipcode;
    }


}