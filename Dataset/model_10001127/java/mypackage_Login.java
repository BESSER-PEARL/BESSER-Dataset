




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class mypackage_Login  {

    private String securityAnswer;
    private LocalDate lastLoginTime;
    private String username;
    private String securityQuestion;
    private String password;



    public mypackage_Login(
        String securityAnswer,        LocalDate lastLoginTime,        String username,        String securityQuestion,        String password    ) {
        this.securityAnswer = securityAnswer;
        this.lastLoginTime = lastLoginTime;
        this.username = username;
        this.securityQuestion = securityQuestion;
        this.password = password;
    }


    public String getSecurityanswer() {
        return securityAnswer;
    }

    public void setSecurityanswer(String securityAnswer) {
        this.securityAnswer = securityAnswer;
    }
    public LocalDate getLastlogintime() {
        return lastLoginTime;
    }

    public void setLastlogintime(LocalDate lastLoginTime) {
        this.lastLoginTime = lastLoginTime;
    }
    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }
    public String getSecurityquestion() {
        return securityQuestion;
    }

    public void setSecurityquestion(String securityQuestion) {
        this.securityQuestion = securityQuestion;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }


}