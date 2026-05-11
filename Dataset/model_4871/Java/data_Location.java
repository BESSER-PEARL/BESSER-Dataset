





import java.util.List;
import java.util.ArrayList;

public class data_Location extends MetaInformation {

    private String state;
    private String country;
    private String latitude;
    private String houseNumber;
    private String zipCode;
    private String longitude;
    private String city;
    private String street;



    public data_Location(
        String state,        String country,        String latitude,        String houseNumber,        String zipCode,        String longitude,        String city,        String street    ) {
        super(
        );
        this.state = state;
        this.country = country;
        this.latitude = latitude;
        this.houseNumber = houseNumber;
        this.zipCode = zipCode;
        this.longitude = longitude;
        this.city = city;
        this.street = street;
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
    public String getLatitude() {
        return latitude;
    }

    public void setLatitude(String latitude) {
        this.latitude = latitude;
    }
    public String getHousenumber() {
        return houseNumber;
    }

    public void setHousenumber(String houseNumber) {
        this.houseNumber = houseNumber;
    }
    public String getZipcode() {
        return zipCode;
    }

    public void setZipcode(String zipCode) {
        this.zipCode = zipCode;
    }
    public String getLongitude() {
        return longitude;
    }

    public void setLongitude(String longitude) {
        this.longitude = longitude;
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


}