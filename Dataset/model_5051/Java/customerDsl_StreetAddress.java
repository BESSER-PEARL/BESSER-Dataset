





import java.util.List;
import java.util.ArrayList;

public class customerDsl_StreetAddress extends Address {

    private String street;
    private String city;



    public customerDsl_StreetAddress(
        String street,        String city    ) {
        super(
        );
        this.street = street;
        this.city = city;
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


}