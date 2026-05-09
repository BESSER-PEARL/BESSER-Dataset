





import java.util.List;
import java.util.ArrayList;

public class decobat_Customer  {

    private String phone;
    private String name;
    private String code;
    private String email;
    private String zip;
    private String address;
    private String fax;
    private String city;
    private String country;





    private decobat_Project decobat_project;


    public decobat_Customer(
        String phone,        String name,        String code,        String email,        String zip,        String address,        String fax,        String city,        String country    ) {
        this.phone = phone;
        this.name = name;
        this.code = code;
        this.email = email;
        this.zip = zip;
        this.address = address;
        this.fax = fax;
        this.city = city;
        this.country = country;
    }


    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
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
    public String getCountry() {
        return country;
    }

    public void setCountry(String country) {
        this.country = country;
    }

    public decobat_Project getDecobat_project() {
        return decobat_project;
    }

    public void setDecobat_project(decobat_Project decobat_project) {
        this.decobat_project = decobat_project;
    }

}