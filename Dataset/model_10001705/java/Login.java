




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Login  {

    private String username;
    private LocalDate lastLoginTime;
    private String password;



    public Login(
        String username,        LocalDate lastLoginTime,        String password    ) {
        this.username = username;
        this.lastLoginTime = lastLoginTime;
        this.password = password;
    }


    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }
    public LocalDate getLastlogintime() {
        return lastLoginTime;
    }

    public void setLastlogintime(LocalDate lastLoginTime) {
        this.lastLoginTime = lastLoginTime;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }


}