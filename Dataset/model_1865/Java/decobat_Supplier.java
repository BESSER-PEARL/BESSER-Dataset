





import java.util.List;
import java.util.ArrayList;

public class decobat_Supplier  {

    private String address;
    private String phone;
    private String zip;
    private String fax;
    private String email;
    private String city;
    private String country;
    private String code;
    private String name;





    private decobat_Product decobat_product;


    public decobat_Supplier(
        String address,        String phone,        String zip,        String fax,        String email,        String city,        String country,        String code,        String name    ) {
        this.address = address;
        this.phone = phone;
        this.zip = zip;
        this.fax = fax;
        this.email = email;
        this.city = city;
        this.country = country;
        this.code = code;
        this.name = name;
    }


    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
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
    public String getFax() {
        return fax;
    }

    public void setFax(String fax) {
        this.fax = fax;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }
    public String getCountry() {
        return country;
    }

    public void setCountry(String country) {
        this.country = country;
    }
    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public decobat_Product getDecobat_product() {
        return decobat_product;
    }

    public void setDecobat_product(decobat_Product decobat_product) {
        this.decobat_product = decobat_product;
    }

}