





import java.util.List;
import java.util.ArrayList;

public class chef  {

    private int Employee_ID;
    private String passowrd;
    private String Name;
    private int Room_no;
    private String Email;



    public chef(
        int Employee_ID,        String passowrd,        String Name,        int Room_no,        String Email    ) {
        this.Employee_ID = Employee_ID;
        this.passowrd = passowrd;
        this.Name = Name;
        this.Room_no = Room_no;
        this.Email = Email;
    }


    public int getEmployee_id() {
        return Employee_ID;
    }

    public void setEmployee_id(int Employee_ID) {
        this.Employee_ID = Employee_ID;
    }
    public String getPassowrd() {
        return passowrd;
    }

    public void setPassowrd(String passowrd) {
        this.passowrd = passowrd;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public int getRoom_no() {
        return Room_no;
    }

    public void setRoom_no(int Room_no) {
        this.Room_no = Room_no;
    }
    public String getEmail() {
        return Email;
    }

    public void setEmail(String Email) {
        this.Email = Email;
    }


}