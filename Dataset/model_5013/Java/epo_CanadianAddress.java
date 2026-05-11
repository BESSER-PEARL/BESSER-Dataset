





import java.util.List;
import java.util.ArrayList;

public class epo_CanadianAddress extends Address {

    private String postalCode;
    private String province;
    private String city;
    private String street;



    public epo_CanadianAddress(
        String postalCode,        String province,        String city,        String street    ) {
        super(
        );
        this.postalCode = postalCode;
        this.province = province;
        this.city = city;
        this.street = street;
    }


    public String getPostalcode() {
        return postalCode;
    }

    public void setPostalcode(String postalCode) {
        this.postalCode = postalCode;
    }
    public String getProvince() {
        return province;
    }

    public void setProvince(String province) {
        this.province = province;
    }
    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }
    public String getStreet() {
        return street;
    }

    public void setStreet(String street) {
        this.street = street;
    }


}