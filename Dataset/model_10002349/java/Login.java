




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Login  {

    private LocalDate lastLoginTime;
    private String password;
    private String username;
    private String securityAnswer;
    private String securityQuestion;





    private Patient patient;


    public Login(
        LocalDate lastLoginTime,        String password,        String username,        String securityAnswer,        String securityQuestion    ) {
        this.lastLoginTime = lastLoginTime;
        this.password = password;
        this.username = username;
        this.securityAnswer = securityAnswer;
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

    public Patient getPatient() {
        return patient;
    }

    public void setPatient(Patient patient) {
        this.patient = patient;
    }

}