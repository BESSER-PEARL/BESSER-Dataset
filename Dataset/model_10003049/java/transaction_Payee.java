





import java.util.List;
import java.util.ArrayList;

public class transaction_Payee  {

    private String email;
    private String accountNum;
    private String zipcode;
    private String name;
    private String state;
    private String city;
    private String phoneNum;
    private String address2;
    private String country;
    private String address1;



    public transaction_Payee(
        String email,        String accountNum,        String zipcode,        String name,        String state,        String city,        String phoneNum,        String address2,        String country,        String address1    ) {
        this.email = email;
        this.accountNum = accountNum;
        this.zipcode = zipcode;
        this.name = name;
        this.state = state;
        this.city = city;
        this.phoneNum = phoneNum;
        this.address2 = address2;
        this.country = country;
        this.address1 = address1;
    }


    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getAccountnum() {
        return accountNum;
    }

    public void setAccountnum(String accountNum) {
        this.accountNum = accountNum;
    }
    public String getZipcode() {
        return zipcode;
    }

    public void setZipcode(String zipcode) {
        this.zipcode = zipcode;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }
    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }
    public String getPhonenum() {
        return phoneNum;
    }

    public void setPhonenum(String phoneNum) {
        this.phoneNum = phoneNum;
    }
    public String getAddress2() {
        return address2;
    }

    public void setAddress2(String address2) {
        this.address2 = address2;
    }
    public String getCountry() {
        return country;
    }

    public void setCountry(String country) {
        this.country = country;
    }
    public String getAddress1() {
        return address1;
    }

    public void setAddress1(String address1) {
        this.address1 = address1;
    }


}