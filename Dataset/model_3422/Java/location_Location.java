





import java.util.List;
import java.util.ArrayList;

public class location_Location  {

    private String street;
    private String state;
    private String city;
    private String altitudeMode;
    private float longitude;
    private String phoneNumber;
    private String country;
    private String description;
    private String postalCode;
    private float altitude;
    private String name;
    private float latitude;
    private String comments;





    private List<location_Area> location_areas;


    public location_Location(
        String street,        String state,        String city,        String altitudeMode,        float longitude,        String phoneNumber,        String country,        String description,        String postalCode,        float altitude,        String name,        float latitude,        String comments    ) {
        this.street = street;
        this.state = state;
        this.city = city;
        this.altitudeMode = altitudeMode;
        this.longitude = longitude;
        this.phoneNumber = phoneNumber;
        this.country = country;
        this.description = description;
        this.postalCode = postalCode;
        this.altitude = altitude;
        this.name = name;
        this.latitude = latitude;
        this.comments = comments;
        this.location_areas = new ArrayList<>();
    }

    public location_Location(
        String street,        String state,        String city,        String altitudeMode,        float longitude,        String phoneNumber,        String country,        String description,        String postalCode,        float altitude,        String name,        float latitude,        String comments        ArrayList<location_Area> location_areas    ) {
        this.street = street;
        this.state = state;
        this.city = city;
        this.altitudeMode = altitudeMode;
        this.longitude = longitude;
        this.phoneNumber = phoneNumber;
        this.country = country;
        this.description = description;
        this.postalCode = postalCode;
        this.altitude = altitude;
        this.name = name;
        this.latitude = latitude;
        this.comments = comments;
        this.location_areas = location_areas;
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
    public String getCountry() {
        return country;
    }

    public void setCountry(String country) {
        this.country = country;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getPostalcode() {
        return postalCode;
    }

    public void setPostalcode(String postalCode) {
        this.postalCode = postalCode;
    }
    public float getAltitude() {
        return altitude;
    }

    public void setAltitude(float altitude) {
        this.altitude = altitude;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public float getLatitude() {
        return latitude;
    }

    public void setLatitude(float latitude) {
        this.latitude = latitude;
    }
    public String getComments() {
        return comments;
    }

    public void setComments(String comments) {
        this.comments = comments;
    }

    public List<location_Area> getLocation_areas() {
        return location_areas;
    }

    public void addLocation_area(Location_area location_area) {
        this.location_areas.add(location_area);
    }

}