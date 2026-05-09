





import java.util.List;
import java.util.ArrayList;

public class gedcoml_PostAddress extends Address {

    private String city;
    private String postcode;
    private String street;



    public gedcoml_PostAddress(
        String city,        String postcode,        String street    ) {
        super(
        );
        this.city = city;
        this.postcode = postcode;
        this.street = street;
    }


    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }
    public String getPostcode() {
        return postcode;
    }

    public void setPostcode(String postcode) {
        this.postcode = postcode;
    }
    public String getStreet() {
        return street;
    }

    public void setStreet(String street) {
        this.street = street;
    }


}