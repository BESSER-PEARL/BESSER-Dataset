





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String phone;
    private String address;
    private String email;





    private Account account;




    private WebUser webuser;


    public Customer(
        String phone,        String address,        String email    ) {
        this.phone = phone;
        this.address = address;
        this.email = email;
    }


    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
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

    public Account getAccount() {
        return account;
    }

    public void setAccount(Account account) {
        this.account = account;
    }
    public WebUser getWebuser() {
        return webuser;
    }

    public void setWebuser(WebUser webuser) {
        this.webuser = webuser;
    }

}