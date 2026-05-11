





import java.util.List;
import java.util.ArrayList;

public class bank_PostalAddress extends ContactMethod {

    private String line2;
    private String stateProvince;
    private String country;
    private String line1;
    private String city;
    private String postalCode;



    public bank_PostalAddress(
        String line2,        String stateProvince,        String country,        String line1,        String city,        String postalCode    ) {
        super(
        );
        this.line2 = line2;
        this.stateProvince = stateProvince;
        this.country = country;
        this.line1 = line1;
        this.city = city;
        this.postalCode = postalCode;
    }


    public String getLine2() {
        return line2;
    }

    public void setLine2(String line2) {
        this.line2 = line2;
    }
    public String getStateprovince() {
        return stateProvince;
    }

    public void setStateprovince(String stateProvince) {
        this.stateProvince = stateProvince;
    }
    public String getCountry() {
        return country;
    }

    public void setCountry(String country) {
        this.country = country;
    }
    public String getLine1() {
        return line1;
    }

    public void setLine1(String line1) {
        this.line1 = line1;
    }
    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }
    public String getPostalcode() {
        return postalCode;
    }

    public void setPostalcode(String postalCode) {
        this.postalCode = postalCode;
    }


}