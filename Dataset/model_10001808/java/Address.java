





import java.util.List;
import java.util.ArrayList;

public class Address  {

    private String suburb;
    private String state;
    private String postcode;
    private None country;
    private String street;



    public Address(
        String suburb,        String state,        String postcode,        None country,        String street    ) {
        this.suburb = suburb;
        this.state = state;
        this.postcode = postcode;
        this.country = country;
        this.street = street;
    }


    public String getSuburb() {
        return suburb;
    }

    public void setSuburb(String suburb) {
        this.suburb = suburb;
    }
    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }
    public String getPostcode() {
        return postcode;
    }

    public void setPostcode(String postcode) {
        this.postcode = postcode;
    }
    public None getCountry() {
        return country;
    }

    public void setCountry(None country) {
        this.country = country;
    }
    public String getStreet() {
        return street;
    }

    public void setStreet(String street) {
        this.street = street;
    }


}