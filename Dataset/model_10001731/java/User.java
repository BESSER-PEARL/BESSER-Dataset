





import java.util.List;
import java.util.ArrayList;

public class User  {

    private String Mail;
    private String attribute;
    private String Address;
    private String RegistrationDate;
    private boolean Active;
    private int UserCode;
    private int Phone;



    public User(
        String Mail,        String attribute,        String Address,        String RegistrationDate,        boolean Active,        int UserCode,        int Phone    ) {
        this.Mail = Mail;
        this.attribute = attribute;
        this.Address = Address;
        this.RegistrationDate = RegistrationDate;
        this.Active = Active;
        this.UserCode = UserCode;
        this.Phone = Phone;
    }


    public String getMail() {
        return Mail;
    }

    public void setMail(String Mail) {
        this.Mail = Mail;
    }
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }
    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }
    public String getRegistrationdate() {
        return RegistrationDate;
    }

    public void setRegistrationdate(String RegistrationDate) {
        this.RegistrationDate = RegistrationDate;
    }
    public boolean getActive() {
        return Active;
    }

    public void setActive(boolean Active) {
        this.Active = Active;
    }
    public int getUsercode() {
        return UserCode;
    }

    public void setUsercode(int UserCode) {
        this.UserCode = UserCode;
    }
    public int getPhone() {
        return Phone;
    }

    public void setPhone(int Phone) {
        this.Phone = Phone;
    }


}