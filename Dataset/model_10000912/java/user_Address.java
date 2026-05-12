





import java.util.List;
import java.util.ArrayList;

public class user_Address  {

    private None country;
    private String state;
    private String suburb;
    private String street;
    private String postcode;



    public user_Address(
        None country,        String state,        String suburb,        String street,        String postcode    ) {
        this.country = country;
        this.state = state;
        this.suburb = suburb;
        this.street = street;
        this.postcode = postcode;
    }


    public None getCountry() {
        return country;
    }

    public void setCountry(None country) {
        this.country = country;
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
    public String getStreet() {
        return street;
    }

    public void setStreet(String street) {
        this.street = street;
    }
    public String getPostcode() {
        return postcode;
    }

    public void setPostcode(String postcode) {
        this.postcode = postcode;
    }


}