





import java.util.List;
import java.util.ArrayList;

public class data_Location extends MetaInformation {

    private String longitude;
    private String zipCode;
    private String street;
    private String country;
    private String state;
    private String latitude;
    private String city;
    private String houseNumber;



    public data_Location(
        String longitude,        String zipCode,        String street,        String country,        String state,        String latitude,        String city,        String houseNumber    ) {
        super(
        );
        this.longitude = longitude;
        this.zipCode = zipCode;
        this.street = street;
        this.country = country;
        this.state = state;
        this.latitude = latitude;
        this.city = city;
        this.houseNumber = houseNumber;
    }


    public String getLongitude() {
        return longitude;
    }

    public void setLongitude(String longitude) {
        this.longitude = longitude;
    }
    public String getZipcode() {
        return zipCode;
    }

    public void setZipcode(String zipCode) {
        this.zipCode = zipCode;
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
    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }
    public String getLatitude() {
        return latitude;
    }

    public void setLatitude(String latitude) {
        this.latitude = latitude;
    }
    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }
    public String getHousenumber() {
        return houseNumber;
    }

    public void setHousenumber(String houseNumber) {
        this.houseNumber = houseNumber;
    }


}