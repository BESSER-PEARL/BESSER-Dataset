





import java.util.List;
import java.util.ArrayList;

public class decobat_Customer  {

    private String country;
    private String email;
    private String phone;
    private String name;
    private String city;
    private String zip;
    private String fax;
    private String address;
    private String code;





    private decobat_Project decobat_project;


    public decobat_Customer(
        String country,        String email,        String phone,        String name,        String city,        String zip,        String fax,        String address,        String code    ) {
        this.country = country;
        this.email = email;
        this.phone = phone;
        this.name = name;
        this.city = city;
        this.zip = zip;
        this.fax = fax;
        this.address = address;
        this.code = code;
    }


    public String getCountry() {
        return country;
    }

    public void setCountry(String country) {
        this.country = country;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
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
    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
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
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }

    public decobat_Project getDecobat_project() {
        return decobat_project;
    }

    public void setDecobat_project(decobat_Project decobat_project) {
        this.decobat_project = decobat_project;
    }

}