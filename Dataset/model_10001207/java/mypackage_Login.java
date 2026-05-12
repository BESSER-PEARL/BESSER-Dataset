




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class mypackage_Login  {

    private LocalDate lastLoginTime;
    private String securityAnswer;
    private String securityQuestion;
    private String username;
    private String password;



    public mypackage_Login(
        LocalDate lastLoginTime,        String securityAnswer,        String securityQuestion,        String username,        String password    ) {
        this.lastLoginTime = lastLoginTime;
        this.securityAnswer = securityAnswer;
        this.securityQuestion = securityQuestion;
        this.username = username;
        this.password = password;
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
    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }


}