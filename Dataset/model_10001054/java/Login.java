




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Login  {

    private String password;
    private String securityAnswer;
    private String securityQuestion;
    private LocalDate lastLoginTime;
    private String username;





    private Customer customer;


    public Login(
        String password,        String securityAnswer,        String securityQuestion,        LocalDate lastLoginTime,        String username    ) {
        this.password = password;
        this.securityAnswer = securityAnswer;
        this.securityQuestion = securityQuestion;
        this.lastLoginTime = lastLoginTime;
        this.username = username;
    }


    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
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
    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }

}