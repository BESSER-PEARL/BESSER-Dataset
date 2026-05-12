





import java.util.List;
import java.util.ArrayList;

public class user_Address  {

    private String state;
    private String suburb;
    private String postcode;
    private String street;
    private None country;





    private user_User user_user;


    public user_Address(
        String state,        String suburb,        String postcode,        String street,        None country    ) {
        this.state = state;
        this.suburb = suburb;
        this.postcode = postcode;
        this.street = street;
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
    public String getPostcode() {
        return postcode;
    }

    public void setPostcode(String postcode) {
        this.postcode = postcode;
    }
    public String getStreet() {
        return street;
    }

    public void setStreet(String street) {
        this.street = street;
    }
    public None getCountry() {
        return country;
    }

    public void setCountry(None country) {
        this.country = country;
    }

    public user_User getUser_user() {
        return user_user;
    }

    public void setUser_user(user_User user_user) {
        this.user_user = user_user;
    }

}