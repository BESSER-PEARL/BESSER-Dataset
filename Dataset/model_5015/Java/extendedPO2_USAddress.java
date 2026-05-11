





import java.util.List;
import java.util.ArrayList;

public class extendedPO2_USAddress extends Address {

    private String state;
    private String street;
    private int zip;
    private String city;



    public extendedPO2_USAddress(
        String state,        String street,        int zip,        String city    ) {
        super(
        );
        this.state = state;
        this.street = street;
        this.zip = zip;
        this.city = city;
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
    public int getZip() {
        return zip;
    }

    public void setZip(int zip) {
        this.zip = zip;
    }
    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }


}