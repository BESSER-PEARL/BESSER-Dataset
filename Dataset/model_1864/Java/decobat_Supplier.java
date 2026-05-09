





import java.util.List;
import java.util.ArrayList;

public class decobat_Supplier  {

    private String name;
    private String phone;
    private String zip;
    private String address;
    private String fax;
    private String city;
    private String email;
    private String code;
    private String country;





    private decobat_Product decobat_product;


    public decobat_Supplier(
        String name,        String phone,        String zip,        String address,        String fax,        String city,        String email,        String code,        String country    ) {
        this.name = name;
        this.phone = phone;
        this.zip = zip;
        this.address = address;
        this.fax = fax;
        this.city = city;
        this.email = email;
        this.code = code;
        this.country = country;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }
    public String getZip() {
        return zip;
    }

    public void setZip(String zip) {
        this.zip = zip;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getFax() {
        return fax;
    }

    public void setFax(String fax) {
        this.fax = fax;
    }
    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }
    public String getCountry() {
        return country;
    }

    public void setCountry(String country) {
        this.country = country;
    }

    public decobat_Product getDecobat_product() {
        return decobat_product;
    }

    public void setDecobat_product(decobat_Product decobat_product) {
        this.decobat_product = decobat_product;
    }

}