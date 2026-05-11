





import java.util.List;
import java.util.ArrayList;

public class epo2_USAddress extends Address {

    private String state;
    private String city;
    private String street;
    private int zip;



    public epo2_USAddress(
        String state,        String city,        String street,        int zip    ) {
        super(
        );
        this.state = state;
        this.city = city;
        this.street = street;
        this.zip = zip;
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
    public String getStreet() {
        return street;
    }

    public void setStreet(String street) {
        this.street = street;
    }
    public int getZip() {
        return zip;
    }

    public void setZip(int zip) {
        this.zip = zip;
    }


}