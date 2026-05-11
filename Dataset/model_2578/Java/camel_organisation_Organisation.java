





import java.util.List;
import java.util.ArrayList;

public class camel_organisation_Organisation extends Entity {

    private String email;
    private String name;
    private String postalAddress;
    private String www;



    public camel_organisation_Organisation(
        String email,        String name,        String postalAddress,        String www    ) {
        super(
        );
        this.email = email;
        this.name = name;
        this.postalAddress = postalAddress;
        this.www = www;
    }


    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getPostaladdress() {
        return postalAddress;
    }

    public void setPostaladdress(String postalAddress) {
        this.postalAddress = postalAddress;
    }
    public String getWww() {
        return www;
    }

    public void setWww(String www) {
        this.www = www;
    }


}