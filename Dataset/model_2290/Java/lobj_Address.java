





import java.util.List;
import java.util.ArrayList;

public class lobj_Address  {

    private String postcode;
    private String fax;
    private String country;
    private String city;
    private String otheraddr;
    private String id;
    private String street;
    private String state;
    private String email;
    private String phone;





    private lobj_Affiliation lobj_affiliation;


    public lobj_Address(
        String postcode,        String fax,        String country,        String city,        String otheraddr,        String id,        String street,        String state,        String email,        String phone    ) {
        this.postcode = postcode;
        this.fax = fax;
        this.country = country;
        this.city = city;
        this.otheraddr = otheraddr;
        this.id = id;
        this.street = street;
        this.state = state;
        this.email = email;
        this.phone = phone;
    }


    public String getPostcode() {
        return postcode;
    }

    public void setPostcode(String postcode) {
        this.postcode = postcode;
    }
    public String getFax() {
        return fax;
    }

    public void setFax(String fax) {
        this.fax = fax;
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
    public String getOtheraddr() {
        return otheraddr;
    }

    public void setOtheraddr(String otheraddr) {
        this.otheraddr = otheraddr;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getStreet() {
        return street;
    }

    public void setStreet(String street) {
        this.street = street;
    }
    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
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

    public lobj_Affiliation getLobj_affiliation() {
        return lobj_affiliation;
    }

    public void setLobj_affiliation(lobj_Affiliation lobj_affiliation) {
        this.lobj_affiliation = lobj_affiliation;
    }

}