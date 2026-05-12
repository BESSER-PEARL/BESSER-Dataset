




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class mypackage_Login  {

    private String securityQuestion;
    private String username;
    private String securityAnswer;
    private String password;
    private LocalDate lastLoginTime;



    public mypackage_Login(
        String securityQuestion,        String username,        String securityAnswer,        String password,        LocalDate lastLoginTime    ) {
        this.securityQuestion = securityQuestion;
        this.username = username;
        this.securityAnswer = securityAnswer;
        this.password = password;
        this.lastLoginTime = lastLoginTime;
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
    public String getSecurityanswer() {
        return securityAnswer;
    }

    public void setSecurityanswer(String securityAnswer) {
        this.securityAnswer = securityAnswer;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public LocalDate getLastlogintime() {
        return lastLoginTime;
    }

    public void setLastlogintime(LocalDate lastLoginTime) {
        this.lastLoginTime = lastLoginTime;
    }


}