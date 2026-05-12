




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class mypackage_Login  {

    private String username;
    private String securityAnswer;
    private String securityQuestion;
    private LocalDate lastLoginTime;
    private String password;



    public mypackage_Login(
        String username,        String securityAnswer,        String securityQuestion,        LocalDate lastLoginTime,        String password    ) {
        this.username = username;
        this.securityAnswer = securityAnswer;
        this.securityQuestion = securityQuestion;
        this.lastLoginTime = lastLoginTime;
        this.password = password;
    }


    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
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