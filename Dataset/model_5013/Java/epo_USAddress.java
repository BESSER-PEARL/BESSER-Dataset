





import java.util.List;
import java.util.ArrayList;

public class epo_USAddress extends Address {

    private String city;
    private int zip;
    private String state;
    private String street;



    public epo_USAddress(
        String city,        int zip,        String state,        String street    ) {
        super(
        );
        this.city = city;
        this.zip = zip;
        this.state = state;
        this.street = street;
    }


    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }
    public int getZip() {
        return zip;
    }

    public void setZip(int zip) {
        this.zip = zip;
    }
    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }
    public String getStreet() {
        return street;
    }

    public void setStreet(String street) {
        this.street = street;
    }


}