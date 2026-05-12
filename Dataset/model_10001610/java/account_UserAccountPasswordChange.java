





import java.util.List;
import java.util.ArrayList;

public class account_UserAccountPasswordChange  {

    private String oldPassword;
    private String newPassword;
    private String email;



    public account_UserAccountPasswordChange(
        String oldPassword,        String newPassword,        String email    ) {
        this.oldPassword = oldPassword;
        this.newPassword = newPassword;
        this.email = email;
    }


    public String getOldpassword() {
        return oldPassword;
    }

    public void setOldpassword(String oldPassword) {
        this.oldPassword = oldPassword;
    }
    public String getNewpassword() {
        return newPassword;
    }

    public void setNewpassword(String newPassword) {
        this.newPassword = newPassword;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }


}