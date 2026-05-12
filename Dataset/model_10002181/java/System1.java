





import java.util.List;
import java.util.ArrayList;

public class System1  {

    private String Password;
    private String Email;
    private String WebAdmin_or_owner;





    private Storage1 storage1;


    public System1(
        String Password,        String Email,        String WebAdmin_or_owner    ) {
        this.Password = Password;
        this.Email = Email;
        this.WebAdmin_or_owner = WebAdmin_or_owner;
    }


    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }
    public String getEmail() {
        return Email;
    }

    public void setEmail(String Email) {
        this.Email = Email;
    }
    public String getWebadmin_or_owner() {
        return WebAdmin_or_owner;
    }

    public void setWebadmin_or_owner(String WebAdmin_or_owner) {
        this.WebAdmin_or_owner = WebAdmin_or_owner;
    }

    public Storage1 getStorage1() {
        return storage1;
    }

    public void setStorage1(Storage1 storage1) {
        this.storage1 = storage1;
    }

}