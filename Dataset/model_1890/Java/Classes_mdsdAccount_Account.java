





import java.util.List;
import java.util.ArrayList;

public class Classes_mdsdAccount_Account  {

    private String email;
    private String password;
    private boolean isLoggedIn;
    private String name;
    private String accountID;



    public Classes_mdsdAccount_Account(
        String email,        String password,        boolean isLoggedIn,        String name,        String accountID    ) {
        this.email = email;
        this.password = password;
        this.isLoggedIn = isLoggedIn;
        this.name = name;
        this.accountID = accountID;
    }


    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public boolean getIsloggedin() {
        return isLoggedIn;
    }

    public void setIsloggedin(boolean isLoggedIn) {
        this.isLoggedIn = isLoggedIn;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAccountid() {
        return accountID;
    }

    public void setAccountid(String accountID) {
        this.accountID = accountID;
    }


}