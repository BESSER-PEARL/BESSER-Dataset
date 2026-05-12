





import java.util.List;
import java.util.ArrayList;

public class user_Address  {

    private String street;
    private String country;
    private String postcode;
    private String state;
    private String suburb;



    public user_Address(
        String street,        String country,        String postcode,        String state,        String suburb    ) {
        this.street = street;
        this.country = country;
        this.postcode = postcode;
        this.state = state;
        this.suburb = suburb;
    }


    public String getStreet() {
        return street;
    }

    public void setStreet(String street) {
        this.street = street;
    }
    public String getCountry() {
        return country;
    }

    public void setCountry(String country) {
        this.country = country;
    }
    public String getPostcode() {
        return postcode;
    }

    public void setPostcode(String postcode) {
        this.postcode = postcode;
    }
    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }
    public String getSuburb() {
        return suburb;
    }

    public void setSuburb(String suburb) {
        this.suburb = suburb;
    }


}