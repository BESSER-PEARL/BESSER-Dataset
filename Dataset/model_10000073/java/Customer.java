





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private boolean emailVerified;
    private String address;
    private String email;
    private String phone;
    private boolean phoneVeified;



    public Customer(
        boolean emailVerified,        String address,        String email,        String phone,        boolean phoneVeified    ) {
        this.emailVerified = emailVerified;
        this.address = address;
        this.email = email;
        this.phone = phone;
        this.phoneVeified = phoneVeified;
    }


    public boolean getEmailverified() {
        return emailVerified;
    }

    public void setEmailverified(boolean emailVerified) {
        this.emailVerified = emailVerified;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
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
    public boolean getPhoneveified() {
        return phoneVeified;
    }

    public void setPhoneveified(boolean phoneVeified) {
        this.phoneVeified = phoneVeified;
    }


}