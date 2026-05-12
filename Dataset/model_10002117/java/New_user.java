





import java.util.List;
import java.util.ArrayList;

public class New_user  {

    private int Student_ID;
    private String Major;
    private int Contact_No;
    private String Last_Name;
    private int Student_ID1;
    private String First_name;





    private Login login;


    public New_user(
        int Student_ID,        String Major,        int Contact_No,        String Last_Name,        int Student_ID1,        String First_name    ) {
        this.Student_ID = Student_ID;
        this.Major = Major;
        this.Contact_No = Contact_No;
        this.Last_Name = Last_Name;
        this.Student_ID1 = Student_ID1;
        this.First_name = First_name;
    }


    public int getStudent_id() {
        return Student_ID;
    }

    public void setStudent_id(int Student_ID) {
        this.Student_ID = Student_ID;
    }
    public String getMajor() {
        return Major;
    }

    public void setMajor(String Major) {
        this.Major = Major;
    }
    public int getContact_no() {
        return Contact_No;
    }

    public void setContact_no(int Contact_No) {
        this.Contact_No = Contact_No;
    }
    public String getLast_name() {
        return Last_Name;
    }

    public void setLast_name(String Last_Name) {
        this.Last_Name = Last_Name;
    }
    public int getStudent_id1() {
        return Student_ID1;
    }

    public void setStudent_id1(int Student_ID1) {
        this.Student_ID1 = Student_ID1;
    }
    public String getFirst_name() {
        return First_name;
    }

    public void setFirst_name(String First_name) {
        this.First_name = First_name;
    }

    public Login getLogin() {
        return login;
    }

    public void setLogin(Login login) {
        this.login = login;
    }

}