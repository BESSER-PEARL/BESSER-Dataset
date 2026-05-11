





import java.util.List;
import java.util.ArrayList;

public class data_Location extends MetaInformation {

    private String state;
    private String longitude;
    private String street;
    private String country;
    private String zipCode;
    private String houseNumber;
    private String city;
    private String latitude;





    private data_IndoorLocation data_indoorlocation;




    private List<data_IndoorLocation> data_indoorlocations;


    public data_Location(
        String state,        String longitude,        String street,        String country,        String zipCode,        String houseNumber,        String city,        String latitude    ) {
        super(
        );
        this.state = state;
        this.longitude = longitude;
        this.street = street;
        this.country = country;
        this.zipCode = zipCode;
        this.houseNumber = houseNumber;
        this.city = city;
        this.latitude = latitude;
        this.data_indoorlocations = new ArrayList<>();
    }

    public data_Location(
        String state,        String longitude,        String street,        String country,        String zipCode,        String houseNumber,        String city,        String latitude        ArrayList<data_IndoorLocation> data_indoorlocations    ) {
        this.state = state;
        this.longitude = longitude;
        this.street = street;
        this.country = country;
        this.zipCode = zipCode;
        this.houseNumber = houseNumber;
        this.city = city;
        this.latitude = latitude;
        this.data_indoorlocations = data_indoorlocations;
    }

    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }
    public String getLongitude() {
        return longitude;
    }

    public void setLongitude(String longitude) {
        this.longitude = longitude;
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
    public String getZipcode() {
        return zipCode;
    }

    public void setZipcode(String zipCode) {
        this.zipCode = zipCode;
    }
    public String getHousenumber() {
        return houseNumber;
    }

    public void setHousenumber(String houseNumber) {
        this.houseNumber = houseNumber;
    }
    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }
    public String getLatitude() {
        return latitude;
    }

    public void setLatitude(String latitude) {
        this.latitude = latitude;
    }

    public data_IndoorLocation getData_indoorlocation() {
        return data_indoorlocation;
    }

    public void setData_indoorlocation(data_IndoorLocation data_indoorlocation) {
        this.data_indoorlocation = data_indoorlocation;
    }
    public List<data_IndoorLocation> getData_indoorlocations() {
        return data_indoorlocations;
    }

    public void addData_indoorlocation(Data_indoorlocation data_indoorlocation) {
        this.data_indoorlocations.add(data_indoorlocation);
    }

}