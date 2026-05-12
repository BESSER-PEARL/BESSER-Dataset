





import java.util.List;
import java.util.ArrayList;

public class Address  {

    private String country;
    private String city;
    private String state;
    private String street;
    private String postalcode;





    private CustomerInfo customerinfo;


    public Address(
        String country,        String city,        String state,        String street,        String postalcode    ) {
        this.country = country;
        this.city = city;
        this.state = state;
        this.street = street;
        this.postalcode = postalcode;
    }


    public String getCountry() {
        return country;
    }

    public void setCountry(String country) {
        this.country = country;
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
    public String getStreet() {
        return street;
    }

    public void setStreet(String street) {
        this.street = street;
    }
    public String getPostalcode() {
        return postalcode;
    }

    public void setPostalcode(String postalcode) {
        this.postalcode = postalcode;
    }

    public CustomerInfo getCustomerinfo() {
        return customerinfo;
    }

    public void setCustomerinfo(CustomerInfo customerinfo) {
        this.customerinfo = customerinfo;
    }

}