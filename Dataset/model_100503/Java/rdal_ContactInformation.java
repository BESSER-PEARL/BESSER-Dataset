





import java.util.List;
import java.util.ArrayList;

public class rdal_ContactInformation extends IdentifiedElement {

    private String address;
    private String country;
    private String email;
    private String phoneNumber;





    private rdal_Stakeholder rdal_stakeholder;


    public rdal_ContactInformation(
        String address,        String country,        String email,        String phoneNumber    ) {
        super(
        );
        this.address = address;
        this.country = country;
        this.email = email;
        this.phoneNumber = phoneNumber;
    }


    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
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
    public String getPhonenumber() {
        return phoneNumber;
    }

    public void setPhonenumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
    }

    public rdal_Stakeholder getRdal_stakeholder() {
        return rdal_stakeholder;
    }

    public void setRdal_stakeholder(rdal_Stakeholder rdal_stakeholder) {
        this.rdal_stakeholder = rdal_stakeholder;
    }

}