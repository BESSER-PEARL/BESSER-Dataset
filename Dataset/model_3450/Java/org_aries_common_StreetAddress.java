





import java.util.List;
import java.util.ArrayList;

public class org_aries_common_StreetAddress  {

    private String latitude;
    private String street;
    private String id;
    private String longitude;
    private String country;
    private String state;
    private String city;





    private ZipCode zipcode;


    public org_aries_common_StreetAddress(
        String latitude,        String street,        String id,        String longitude,        String country,        String state,        String city    ) {
        this.latitude = latitude;
        this.street = street;
        this.id = id;
        this.longitude = longitude;
        this.country = country;
        this.state = state;
        this.city = city;
    }


    public String getLatitude() {
        return latitude;
    }

    public void setLatitude(String latitude) {
        this.latitude = latitude;
    }
    public String getStreet() {
        return street;
    }

    public void setStreet(String street) {
        this.street = street;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getLongitude() {
        return longitude;
    }

    public void setLongitude(String longitude) {
        this.longitude = longitude;
    }
    public String getCountry() {
        return country;
    }

    public void setCountry(String country) {
        this.country = country;
    }
    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }
    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }

    public ZipCode getZipcode() {
        return zipcode;
    }

    public void setZipcode(ZipCode zipcode) {
        this.zipcode = zipcode;
    }

}