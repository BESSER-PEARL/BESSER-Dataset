




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Manager  {

    private LocalDate Emp_Date_Of_Joint;
    private String Emp_Department;
    private String Emp_Position;
    private float Mng_Salary;
    private int Mng_Id;
    private String Mng_Email;
    private String Mng_ContactNo;
    private LocalDate Emp_DOB;
    private String Emp_NIC;
    private String Emp_Address;
    private String Mng_Name;



    public Manager(
        LocalDate Emp_Date_Of_Joint,        String Emp_Department,        String Emp_Position,        float Mng_Salary,        int Mng_Id,        String Mng_Email,        String Mng_ContactNo,        LocalDate Emp_DOB,        String Emp_NIC,        String Emp_Address,        String Mng_Name    ) {
        this.Emp_Date_Of_Joint = Emp_Date_Of_Joint;
        this.Emp_Department = Emp_Department;
        this.Emp_Position = Emp_Position;
        this.Mng_Salary = Mng_Salary;
        this.Mng_Id = Mng_Id;
        this.Mng_Email = Mng_Email;
        this.Mng_ContactNo = Mng_ContactNo;
        this.Emp_DOB = Emp_DOB;
        this.Emp_NIC = Emp_NIC;
        this.Emp_Address = Emp_Address;
        this.Mng_Name = Mng_Name;
    }


    public LocalDate getEmp_date_of_joint() {
        return Emp_Date_Of_Joint;
    }

    public void setEmp_date_of_joint(LocalDate Emp_Date_Of_Joint) {
        this.Emp_Date_Of_Joint = Emp_Date_Of_Joint;
    }
    public String getEmp_department() {
        return Emp_Department;
    }

    public void setEmp_department(String Emp_Department) {
        this.Emp_Department = Emp_Department;
    }
    public String getEmp_position() {
        return Emp_Position;
    }

    public void setEmp_position(String Emp_Position) {
        this.Emp_Position = Emp_Position;
    }
    public float getMng_salary() {
        return Mng_Salary;
    }

    public void setMng_salary(float Mng_Salary) {
        this.Mng_Salary = Mng_Salary;
    }
    public int getMng_id() {
        return Mng_Id;
    }

    public void setMng_id(int Mng_Id) {
        this.Mng_Id = Mng_Id;
    }
    public String getMng_email() {
        return Mng_Email;
    }

    public void setMng_email(String Mng_Email) {
        this.Mng_Email = Mng_Email;
    }
    public String getMng_contactno() {
        return Mng_ContactNo;
    }

    public void setMng_contactno(String Mng_ContactNo) {
        this.Mng_ContactNo = Mng_ContactNo;
    }
    public LocalDate getEmp_dob() {
        return Emp_DOB;
    }

    public void setEmp_dob(LocalDate Emp_DOB) {
        this.Emp_DOB = Emp_DOB;
    }
    public String getEmp_nic() {
        return Emp_NIC;
    }

    public void setEmp_nic(String Emp_NIC) {
        this.Emp_NIC = Emp_NIC;
    }
    public String getEmp_address() {
        return Emp_Address;
    }

    public void setEmp_address(String Emp_Address) {
        this.Emp_Address = Emp_Address;
    }
    public String getMng_name() {
        return Mng_Name;
    }

    public void setMng_name(String Mng_Name) {
        this.Mng_Name = Mng_Name;
    }


}