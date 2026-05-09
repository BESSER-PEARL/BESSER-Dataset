





import java.util.List;
import java.util.ArrayList;

public class gedcoml_PostAddress extends Address {

    private String street;
    private String city;
    private String postcode;



    public gedcoml_PostAddress(
        String street,        String city,        String postcode    ) {
        super(
        );
        this.street = street;
        this.city = city;
        this.postcode = postcode;
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
    public String getPostcode() {
        return postcode;
    }

    public void setPostcode(String postcode) {
        this.postcode = postcode;
    }


}