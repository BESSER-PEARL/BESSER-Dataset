




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class mypackage_Login  {

    private String securityQuestion;
    private String securityAnswer;
    private LocalDate lastLoginTime;
    private String username;
    private String password;



    public mypackage_Login(
        String securityQuestion,        String securityAnswer,        LocalDate lastLoginTime,        String username,        String password    ) {
        this.securityQuestion = securityQuestion;
        this.securityAnswer = securityAnswer;
        this.lastLoginTime = lastLoginTime;
        this.username = username;
        this.password = password;
    }


    public String getSecurityquestion() {
        return securityQuestion;
    }

    public void setSecurityquestion(String securityQuestion) {
        this.securityQuestion = securityQuestion;
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
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }


}