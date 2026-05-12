




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Login  {

    private String password;
    private LocalDate lastLoginTime;
    private String username;
    private String securityQuestion;
    private String securityAnswer;





    private Customer customer;


    public Login(
        String password,        LocalDate lastLoginTime,        String username,        String securityQuestion,        String securityAnswer    ) {
        this.password = password;
        this.lastLoginTime = lastLoginTime;
        this.username = username;
        this.securityQuestion = securityQuestion;
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
    public String getSecurityanswer() {
        return securityAnswer;
    }

    public void setSecurityanswer(String securityAnswer) {
        this.securityAnswer = securityAnswer;
    }

    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }

}