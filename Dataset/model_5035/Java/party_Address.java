





import java.util.List;
import java.util.ArrayList;

public class party_Address extends ContactInfo {

    private String country;



    public party_Address(
        String country    ) {
        super(
        );
        this.country = country;
    }


    public String getCountry() {
        return country;
    }

    public void setCountry(String country) {
        this.country = country;
    }


}