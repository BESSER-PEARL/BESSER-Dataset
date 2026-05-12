





import java.util.List;
import java.util.ArrayList;

public class author  {

    private String Mail;
    private String Phone;
    private String FamilyName;
    private String GivenName;
    private String Address;



    public author(
        String Mail,        String Phone,        String FamilyName,        String GivenName,        String Address    ) {
        this.Mail = Mail;
        this.Phone = Phone;
        this.FamilyName = FamilyName;
        this.GivenName = GivenName;
        this.Address = Address;
    }


    public String getMail() {
        return Mail;
    }

    public void setMail(String Mail) {
        this.Mail = Mail;
    }
    public String getPhone() {
        return Phone;
    }

    public void setPhone(String Phone) {
        this.Phone = Phone;
    }
    public String getFamilyname() {
        return FamilyName;
    }

    public void setFamilyname(String FamilyName) {
        this.FamilyName = FamilyName;
    }
    public String getGivenname() {
        return GivenName;
    }

    public void setGivenname(String GivenName) {
        this.GivenName = GivenName;
    }
    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }


}