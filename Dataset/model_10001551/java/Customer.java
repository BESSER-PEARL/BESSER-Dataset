





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String Username;
    private String Name;
    private String Contact;
    private String Password;
    private String Address;





    private Web_User web_user;


    public Customer(
        String Username,        String Name,        String Contact,        String Password,        String Address    ) {
        this.Username = Username;
        this.Name = Name;
        this.Contact = Contact;
        this.Password = Password;
        this.Address = Address;
    }


    public String getUsername() {
        return Username;
    }

    public void setUsername(String Username) {
        this.Username = Username;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getContact() {
        return Contact;
    }

    public void setContact(String Contact) {
        this.Contact = Contact;
    }
    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }
    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }

    public Web_User getWeb_user() {
        return web_user;
    }

    public void setWeb_user(Web_User web_user) {
        this.web_user = web_user;
    }

}