





import java.util.List;
import java.util.ArrayList;

public class Location  {

    private String city;
    private int postalCode;
    private String streetAddress;
    private String stateProvince;





    private User user;




    private Country country;


    public Location(
        String city,        int postalCode,        String streetAddress,        String stateProvince    ) {
        this.city = city;
        this.postalCode = postalCode;
        this.streetAddress = streetAddress;
        this.stateProvince = stateProvince;
    }


    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }
    public int getPostalcode() {
        return postalCode;
    }

    public void setPostalcode(int postalCode) {
        this.postalCode = postalCode;
    }
    public String getStreetaddress() {
        return streetAddress;
    }

    public void setStreetaddress(String streetAddress) {
        this.streetAddress = streetAddress;
    }
    public String getStateprovince() {
        return stateProvince;
    }

    public void setStateprovince(String stateProvince) {
        this.stateProvince = stateProvince;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }
    public Country getCountry() {
        return country;
    }

    public void setCountry(Country country) {
        this.country = country;
    }

}