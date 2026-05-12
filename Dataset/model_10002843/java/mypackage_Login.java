




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class mypackage_Login  {

    private String securityAnswer;
    private LocalDate lastLoginTime;
    private String securityQuestion;
    private String password;
    private String username;



    public mypackage_Login(
        String securityAnswer,        LocalDate lastLoginTime,        String securityQuestion,        String password,        String username    ) {
        this.securityAnswer = securityAnswer;
        this.lastLoginTime = lastLoginTime;
        this.securityQuestion = securityQuestion;
        this.password = password;
        this.username = username;
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
    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }


}