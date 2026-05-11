





import java.util.List;
import java.util.ArrayList;

public class epo_USAddress extends Address {

    private String city;
    private String state;
    private int zip;
    private String street;



    public epo_USAddress(
        String city,        String state,        int zip,        String street    ) {
        super(
        );
        this.city = city;
        this.state = state;
        this.zip = zip;
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


}