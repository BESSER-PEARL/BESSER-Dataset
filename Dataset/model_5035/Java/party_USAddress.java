





import java.util.List;
import java.util.ArrayList;

public class party_USAddress extends Address {

    private String zip;
    private String state;
    private String recipient;
    private String street2;
    private String street1;
    private String city;



    public party_USAddress(
        String zip,        String state,        String recipient,        String street2,        String street1,        String city    ) {
        super(
        );
        this.zip = zip;
        this.state = state;
        this.recipient = recipient;
        this.street2 = street2;
        this.street1 = street1;
        this.city = city;
    }


    public String getZip() {
        return zip;
    }

    public void setZip(String zip) {
        this.zip = zip;
    }
    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }
    public String getRecipient() {
        return recipient;
    }

    public void setRecipient(String recipient) {
        this.recipient = recipient;
    }
    public String getStreet2() {
        return street2;
    }

    public void setStreet2(String street2) {
        this.street2 = street2;
    }
    public String getStreet1() {
        return street1;
    }

    public void setStreet1(String street1) {
        this.street1 = street1;
    }
    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }


}