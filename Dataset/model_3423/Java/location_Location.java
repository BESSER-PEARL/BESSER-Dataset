





import java.util.List;
import java.util.ArrayList;

public class location_Location  {

    private float latitude;
    private String country;
    private String street;
    private String postalCode;
    private String name;
    private float longitude;
    private String phoneNumber;
    private String description;
    private String state;
    private String city;
    private String altitudeMode;
    private String comments;
    private float altitude;



    public location_Location(
        float latitude,        String country,        String street,        String postalCode,        String name,        float longitude,        String phoneNumber,        String description,        String state,        String city,        String altitudeMode,        String comments,        float altitude    ) {
        this.latitude = latitude;
        this.country = country;
        this.street = street;
        this.postalCode = postalCode;
        this.name = name;
        this.longitude = longitude;
        this.phoneNumber = phoneNumber;
        this.description = description;
        this.state = state;
        this.city = city;
        this.altitudeMode = altitudeMode;
        this.comments = comments;
        this.altitude = altitude;
    }


    public float getLatitude() {
        return latitude;
    }

    public void setLatitude(float latitude) {
        this.latitude = latitude;
    }
    public String getCountry() {
        return country;
    }

    public void setCountry(String country) {
        this.country = country;
    }
    public String getStreet() {
        return street;
    }

    public void setStreet(String street) {
        this.street = street;
    }
    public String getPostalcode() {
        return postalCode;
    }

    public void setPostalcode(String postalCode) {
        this.postalCode = postalCode;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public float getLongitude() {
        return longitude;
    }

    public void setLongitude(float longitude) {
        this.longitude = longitude;
    }
    public String getPhonenumber() {
        return phoneNumber;
    }

    public void setPhonenumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
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
    public String getAltitudemode() {
        return altitudeMode;
    }

    public void setAltitudemode(String altitudeMode) {
        this.altitudeMode = altitudeMode;
    }
    public String getComments() {
        return comments;
    }

    public void setComments(String comments) {
        this.comments = comments;
    }
    public float getAltitude() {
        return altitude;
    }

    public void setAltitude(float altitude) {
        this.altitude = altitude;
    }


}