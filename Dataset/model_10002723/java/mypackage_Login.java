




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class mypackage_Login  {

    private String password;
    private String username;
    private LocalDate lastLoginTime;
    private String securityAnswer;
    private String securityQuestion;



    public mypackage_Login(
        String password,        String username,        LocalDate lastLoginTime,        String securityAnswer,        String securityQuestion    ) {
        this.password = password;
        this.username = username;
        this.lastLoginTime = lastLoginTime;
        this.securityAnswer = securityAnswer;
        this.securityQuestion = securityQuestion;
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
    public LocalDate getLastlogintime() {
        return lastLoginTime;
    }

    public void setLastlogintime(LocalDate lastLoginTime) {
        this.lastLoginTime = lastLoginTime;
    }
    public String getSecurityanswer() {
        return securityAnswer;
    }

    public void setSecurityanswer(String securityAnswer) {
        this.securityAnswer = securityAnswer;
    }
    public String getSecurityquestion() {
        return securityQuestion;
    }

    public void setSecurityquestion(String securityQuestion) {
        this.securityQuestion = securityQuestion;
    }


}