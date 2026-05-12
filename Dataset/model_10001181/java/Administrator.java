




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Administrator  {

    private int Admin_Id;
    private String Admin_NIC;
    private LocalDate Emp_Date_Of_Joint;
    private String Emp_Position;
    private String Admin_ContactNo;
    private LocalDate Emp_DOB;
    private String Admin_Name;
    private String Emp_Department;
    private String Admin_Email;





    private Manager manager;




    private Login login;




    private Login login;


    public Administrator(
        int Admin_Id,        String Admin_NIC,        LocalDate Emp_Date_Of_Joint,        String Emp_Position,        String Admin_ContactNo,        LocalDate Emp_DOB,        String Admin_Name,        String Emp_Department,        String Admin_Email    ) {
        this.Admin_Id = Admin_Id;
        this.Admin_NIC = Admin_NIC;
        this.Emp_Date_Of_Joint = Emp_Date_Of_Joint;
        this.Emp_Position = Emp_Position;
        this.Admin_ContactNo = Admin_ContactNo;
        this.Emp_DOB = Emp_DOB;
        this.Admin_Name = Admin_Name;
        this.Emp_Department = Emp_Department;
        this.Admin_Email = Admin_Email;
    }


    public int getAdmin_id() {
        return Admin_Id;
    }

    public void setAdmin_id(int Admin_Id) {
        this.Admin_Id = Admin_Id;
    }
    public String getAdmin_nic() {
        return Admin_NIC;
    }

    public void setAdmin_nic(String Admin_NIC) {
        this.Admin_NIC = Admin_NIC;
    }
    public LocalDate getEmp_date_of_joint() {
        return Emp_Date_Of_Joint;
    }

    public void setEmp_date_of_joint(LocalDate Emp_Date_Of_Joint) {
        this.Emp_Date_Of_Joint = Emp_Date_Of_Joint;
    }
    public String getEmp_position() {
        return Emp_Position;
    }

    public void setEmp_position(String Emp_Position) {
        this.Emp_Position = Emp_Position;
    }
    public String getAdmin_contactno() {
        return Admin_ContactNo;
    }

    public void setAdmin_contactno(String Admin_ContactNo) {
        this.Admin_ContactNo = Admin_ContactNo;
    }
    public LocalDate getEmp_dob() {
        return Emp_DOB;
    }

    public void setEmp_dob(LocalDate Emp_DOB) {
        this.Emp_DOB = Emp_DOB;
    }
    public String getAdmin_name() {
        return Admin_Name;
    }

    public void setAdmin_name(String Admin_Name) {
        this.Admin_Name = Admin_Name;
    }
    public String getEmp_department() {
        return Emp_Department;
    }

    public void setEmp_department(String Emp_Department) {
        this.Emp_Department = Emp_Department;
    }
    public String getAdmin_email() {
        return Admin_Email;
    }

    public void setAdmin_email(String Admin_Email) {
        this.Admin_Email = Admin_Email;
    }

    public Manager getManager() {
        return manager;
    }

    public void setManager(Manager manager) {
        this.manager = manager;
    }
    public Login getLogin() {
        return login;
    }

    public void setLogin(Login login) {
        this.login = login;
    }
    public Login getLogin() {
        return login;
    }

    public void setLogin(Login login) {
        this.login = login;
    }

}