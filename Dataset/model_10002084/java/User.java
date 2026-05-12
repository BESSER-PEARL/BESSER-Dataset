





import java.util.List;
import java.util.ArrayList;

public class User  {

    private String Password;
    private int UserId;
    private String Email;
    private String DateOfBirth;
    private String PhoneNumber;
    private String Login;





    private Event event;


    public User(
        String Password,        int UserId,        String Email,        String DateOfBirth,        String PhoneNumber,        String Login    ) {
        this.Password = Password;
        this.UserId = UserId;
        this.Email = Email;
        this.DateOfBirth = DateOfBirth;
        this.PhoneNumber = PhoneNumber;
        this.Login = Login;
    }


    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }
    public int getUserid() {
        return UserId;
    }

    public void setUserid(int UserId) {
        this.UserId = UserId;
    }
    public String getEmail() {
        return Email;
    }

    public void setEmail(String Email) {
        this.Email = Email;
    }
    public String getDateofbirth() {
        return DateOfBirth;
    }

    public void setDateofbirth(String DateOfBirth) {
        this.DateOfBirth = DateOfBirth;
    }
    public String getPhonenumber() {
        return PhoneNumber;
    }

    public void setPhonenumber(String PhoneNumber) {
        this.PhoneNumber = PhoneNumber;
    }
    public String getLogin() {
        return Login;
    }

    public void setLogin(String Login) {
        this.Login = Login;
    }

    public Event getEvent() {
        return event;
    }

    public void setEvent(Event event) {
        this.event = event;
    }

}