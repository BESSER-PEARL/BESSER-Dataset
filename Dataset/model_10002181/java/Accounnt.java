





import java.util.List;
import java.util.ArrayList;

public class Accounnt  {

    private String Accounttype;
    private String password;
    private String Email;
    private String Employee_ID;





    private chef chef;


    public Accounnt(
        String Accounttype,        String password,        String Email,        String Employee_ID    ) {
        this.Accounttype = Accounttype;
        this.password = password;
        this.Email = Email;
        this.Employee_ID = Employee_ID;
    }


    public String getAccounttype() {
        return Accounttype;
    }

    public void setAccounttype(String Accounttype) {
        this.Accounttype = Accounttype;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getEmail() {
        return Email;
    }

    public void setEmail(String Email) {
        this.Email = Email;
    }
    public String getEmployee_id() {
        return Employee_ID;
    }

    public void setEmployee_id(String Employee_ID) {
        this.Employee_ID = Employee_ID;
    }

    public chef getChef() {
        return chef;
    }

    public void setChef(chef chef) {
        this.chef = chef;
    }

}