





import java.util.List;
import java.util.ArrayList;

public class epo_CanadianAddress extends Address {

    private String province;
    private String street;
    private String city;
    private String postalCode;



    public epo_CanadianAddress(
        String province,        String street,        String city,        String postalCode    ) {
        super(
        );
        this.province = province;
        this.street = street;
        this.city = city;
        this.postalCode = postalCode;
    }


    public String getProvince() {
        return province;
    }

    public void setProvince(String province) {
        this.province = province;
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
    public String getPostalcode() {
        return postalCode;
    }

    public void setPostalcode(String postalCode) {
        this.postalCode = postalCode;
    }


}