





import java.util.List;
import java.util.ArrayList;

public class Registration  {

    private String UserName;
    private String Email;
    private String Last_Name;
    private String Password;
    private String Gender;
    private String attribute5;
    private String First_Name;
    private String attribute;



    public Registration(
        String UserName,        String Email,        String Last_Name,        String Password,        String Gender,        String attribute5,        String First_Name,        String attribute    ) {
        this.UserName = UserName;
        this.Email = Email;
        this.Last_Name = Last_Name;
        this.Password = Password;
        this.Gender = Gender;
        this.attribute5 = attribute5;
        this.First_Name = First_Name;
        this.attribute = attribute;
    }


    public String getUsername() {
        return UserName;
    }

    public void setUsername(String UserName) {
        this.UserName = UserName;
    }
    public String getEmail() {
        return Email;
    }

    public void setEmail(String Email) {
        this.Email = Email;
    }
    public String getLast_name() {
        return Last_Name;
    }

    public void setLast_name(String Last_Name) {
        this.Last_Name = Last_Name;
    }
    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }
    public String getGender() {
        return Gender;
    }

    public void setGender(String Gender) {
        this.Gender = Gender;
    }
    public String getAttribute5() {
        return attribute5;
    }

    public void setAttribute5(String attribute5) {
        this.attribute5 = attribute5;
    }
    public String getFirst_name() {
        return First_Name;
    }

    public void setFirst_name(String First_Name) {
        this.First_Name = First_Name;
    }
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }


}