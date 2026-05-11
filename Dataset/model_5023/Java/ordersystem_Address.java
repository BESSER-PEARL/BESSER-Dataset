





import java.util.List;
import java.util.ArrayList;

public class ordersystem_Address  {

    private String city;
    private String province;
    private String apartment;
    private String number;
    private String country;
    private String postalCode;
    private String street;



    public ordersystem_Address(
        String city,        String province,        String apartment,        String number,        String country,        String postalCode,        String street    ) {
        this.city = city;
        this.province = province;
        this.apartment = apartment;
        this.number = number;
        this.country = country;
        this.postalCode = postalCode;
        this.street = street;
    }


    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }
    public String getProvince() {
        return province;
    }

    public void setProvince(String province) {
        this.province = province;
    }
    public String getApartment() {
        return apartment;
    }

    public void setApartment(String apartment) {
        this.apartment = apartment;
    }
    public String getNumber() {
        return number;
    }

    public void setNumber(String number) {
        this.number = number;
    }
    public String getCountry() {
        return country;
    }

    public void setCountry(String country) {
        this.country = country;
    }
    public String getPostalcode() {
        return postalCode;
    }

    public void setPostalcode(String postalCode) {
        this.postalCode = postalCode;
    }
    public String getStreet() {
        return street;
    }

    public void setStreet(String street) {
        this.street = street;
    }


}