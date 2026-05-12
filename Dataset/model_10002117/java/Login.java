





import java.util.List;
import java.util.ArrayList;

public class Login  {

    private String Password;
    private String Email;
    private int Student_ID;



    public Login(
        String Password,        String Email,        int Student_ID    ) {
        this.Password = Password;
        this.Email = Email;
        this.Student_ID = Student_ID;
    }


    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }
    public String getEmail() {
        return Email;
    }

    public void setEmail(String Email) {
        this.Email = Email;
    }
    public int getStudent_id() {
        return Student_ID;
    }

    public void setStudent_id(int Student_ID) {
        this.Student_ID = Student_ID;
    }


}