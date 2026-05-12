




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Login  {

    private LocalDate lastLoginTime;
    private String username;
    private String securityAnswer;
    private String password;
    private String securityQuestion;





    private Customer customer;


    public Login(
        LocalDate lastLoginTime,        String username,        String securityAnswer,        String password,        String securityQuestion    ) {
        this.lastLoginTime = lastLoginTime;
        this.username = username;
        this.securityAnswer = securityAnswer;
        this.password = password;
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
    public String getSecurityquestion() {
        return securityQuestion;
    }

    public void setSecurityquestion(String securityQuestion) {
        this.securityQuestion = securityQuestion;
    }

    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }

}