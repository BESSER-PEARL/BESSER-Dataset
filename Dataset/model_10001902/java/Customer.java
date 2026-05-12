





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String phone;
    private String email;
    private String address;





    private WebUser webuser;




    private Account account;


    public Customer(
        String phone,        String email,        String address    ) {
        this.phone = phone;
        this.email = email;
        this.address = address;
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

    public WebUser getWebuser() {
        return webuser;
    }

    public void setWebuser(WebUser webuser) {
        this.webuser = webuser;
    }
    public Account getAccount() {
        return account;
    }

    public void setAccount(Account account) {
        this.account = account;
    }

}