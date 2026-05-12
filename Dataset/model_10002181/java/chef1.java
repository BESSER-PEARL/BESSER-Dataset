





import java.util.List;
import java.util.ArrayList;

public class chef1  {

    private String Email;
    private String Name;
    private String passowrd;
    private int Employee_ID;
    private int Room_no;



    public chef1(
        String Email,        String Name,        String passowrd,        int Employee_ID,        int Room_no    ) {
        this.Email = Email;
        this.Name = Name;
        this.passowrd = passowrd;
        this.Employee_ID = Employee_ID;
        this.Room_no = Room_no;
    }


    public String getEmail() {
        return Email;
    }

    public void setEmail(String Email) {
        this.Email = Email;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getPassowrd() {
        return passowrd;
    }

    public void setPassowrd(String passowrd) {
        this.passowrd = passowrd;
    }
    public int getEmployee_id() {
        return Employee_ID;
    }

    public void setEmployee_id(int Employee_ID) {
        this.Employee_ID = Employee_ID;
    }
    public int getRoom_no() {
        return Room_no;
    }

    public void setRoom_no(int Room_no) {
        this.Room_no = Room_no;
    }


}