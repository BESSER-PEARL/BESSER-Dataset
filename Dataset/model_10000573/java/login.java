





import java.util.List;
import java.util.ArrayList;

public class login  {

    private String logoutapp;
    private String password;
    private int loginattempt;
    private int lockout;
    private String username;
    private String loginapp;





    private owner_details owner_details;


    public login(
        String logoutapp,        String password,        int loginattempt,        int lockout,        String username,        String loginapp    ) {
        this.logoutapp = logoutapp;
        this.password = password;
        this.loginattempt = loginattempt;
        this.lockout = lockout;
        this.username = username;
        this.loginapp = loginapp;
    }


    public String getLogoutapp() {
        return logoutapp;
    }

    public void setLogoutapp(String logoutapp) {
        this.logoutapp = logoutapp;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public int getLoginattempt() {
        return loginattempt;
    }

    public void setLoginattempt(int loginattempt) {
        this.loginattempt = loginattempt;
    }
    public int getLockout() {
        return lockout;
    }

    public void setLockout(int lockout) {
        this.lockout = lockout;
    }
    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }
    public String getLoginapp() {
        return loginapp;
    }

    public void setLoginapp(String loginapp) {
        this.loginapp = loginapp;
    }

    public owner_details getOwner_details() {
        return owner_details;
    }

    public void setOwner_details(owner_details owner_details) {
        this.owner_details = owner_details;
    }

}