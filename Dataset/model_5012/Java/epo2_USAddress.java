





import java.util.List;
import java.util.ArrayList;

public class epo2_USAddress extends Address {

    private int zip;
    private String street;
    private String city;
    private String state;



    public epo2_USAddress(
        int zip,        String street,        String city,        String state    ) {
        super(
        );
        this.zip = zip;
        this.street = street;
        this.city = city;
        this.state = state;
    }


    public int getZip() {
        return zip;
    }

    public void setZip(int zip) {
        this.zip = zip;
    }
    public String getStreet() {
        return street;
    }

    public void setStreet(String street) {
        this.street = street;
    }
    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }
    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }


}