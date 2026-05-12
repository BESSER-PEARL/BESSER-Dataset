





import java.util.List;
import java.util.ArrayList;

public class SWRC_Person  {

    private String photo;
    private String homepage;
    private String fax;
    private String phone;
    private String email;
    private String address;
    private String name;



    public SWRC_Person(
        String photo,        String homepage,        String fax,        String phone,        String email,        String address,        String name    ) {
        this.photo = photo;
        this.homepage = homepage;
        this.fax = fax;
        this.phone = phone;
        this.email = email;
        this.address = address;
        this.name = name;
    }


    public String getPhoto() {
        return photo;
    }

    public void setPhoto(String photo) {
        this.photo = photo;
    }
    public String getHomepage() {
        return homepage;
    }

    public void setHomepage(String homepage) {
        this.homepage = homepage;
    }
    public String getFax() {
        return fax;
    }

    public void setFax(String fax) {
        this.fax = fax;
    }
    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}