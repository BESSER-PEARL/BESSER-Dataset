




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Login  {

    private String securityQuestion;
    private String password;
    private String username;
    private LocalDate lastLoginTime;
    private String securityAnswer;





    private Customer customer;


    public Login(
        String securityQuestion,        String password,        String username,        LocalDate lastLoginTime,        String securityAnswer    ) {
        this.securityQuestion = securityQuestion;
        this.password = password;
        this.username = username;
        this.lastLoginTime = lastLoginTime;
        this.securityAnswer = securityAnswer;
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

    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }

}