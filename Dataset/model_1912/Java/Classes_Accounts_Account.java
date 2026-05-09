





import java.util.List;
import java.util.ArrayList;

public class Classes_Accounts_Account  {

    private String password;
    private String username;
    private String accountType;



    public Classes_Accounts_Account(
        String password,        String username,        String accountType    ) {
        this.password = password;
        this.username = username;
        this.accountType = accountType;
    }


    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }
    public String getAccounttype() {
        return accountType;
    }

    public void setAccounttype(String accountType) {
        this.accountType = accountType;
    }


}