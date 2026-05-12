




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Employee  {

    private String Emp_NIC;
    private String Emp_Name;
    private String Emp_Department;
    private LocalDate Emp_Date_Of_Joint;
    private String Emp_Address;
    private int Emp_Id;
    private LocalDate Emp_DOB;
    private float Emp_Salary;
    private String Emp_Position;
    private String Emp_ContactNo;
    private String Emp_Email;



    public Employee(
        String Emp_NIC,        String Emp_Name,        String Emp_Department,        LocalDate Emp_Date_Of_Joint,        String Emp_Address,        int Emp_Id,        LocalDate Emp_DOB,        float Emp_Salary,        String Emp_Position,        String Emp_ContactNo,        String Emp_Email    ) {
        this.Emp_NIC = Emp_NIC;
        this.Emp_Name = Emp_Name;
        this.Emp_Department = Emp_Department;
        this.Emp_Date_Of_Joint = Emp_Date_Of_Joint;
        this.Emp_Address = Emp_Address;
        this.Emp_Id = Emp_Id;
        this.Emp_DOB = Emp_DOB;
        this.Emp_Salary = Emp_Salary;
        this.Emp_Position = Emp_Position;
        this.Emp_ContactNo = Emp_ContactNo;
        this.Emp_Email = Emp_Email;
    }


    public String getEmp_nic() {
        return Emp_NIC;
    }

    public void setEmp_nic(String Emp_NIC) {
        this.Emp_NIC = Emp_NIC;
    }
    public String getEmp_name() {
        return Emp_Name;
    }

    public void setEmp_name(String Emp_Name) {
        this.Emp_Name = Emp_Name;
    }
    public String getEmp_department() {
        return Emp_Department;
    }

    public void setEmp_department(String Emp_Department) {
        this.Emp_Department = Emp_Department;
    }
    public LocalDate getEmp_date_of_joint() {
        return Emp_Date_Of_Joint;
    }

    public void setEmp_date_of_joint(LocalDate Emp_Date_Of_Joint) {
        this.Emp_Date_Of_Joint = Emp_Date_Of_Joint;
    }
    public String getEmp_address() {
        return Emp_Address;
    }

    public void setEmp_address(String Emp_Address) {
        this.Emp_Address = Emp_Address;
    }
    public int getEmp_id() {
        return Emp_Id;
    }

    public void setEmp_id(int Emp_Id) {
        this.Emp_Id = Emp_Id;
    }
    public LocalDate getEmp_dob() {
        return Emp_DOB;
    }

    public void setEmp_dob(LocalDate Emp_DOB) {
        this.Emp_DOB = Emp_DOB;
    }
    public float getEmp_salary() {
        return Emp_Salary;
    }

    public void setEmp_salary(float Emp_Salary) {
        this.Emp_Salary = Emp_Salary;
    }
    public String getEmp_position() {
        return Emp_Position;
    }

    public void setEmp_position(String Emp_Position) {
        this.Emp_Position = Emp_Position;
    }
    public String getEmp_contactno() {
        return Emp_ContactNo;
    }

    public void setEmp_contactno(String Emp_ContactNo) {
        this.Emp_ContactNo = Emp_ContactNo;
    }
    public String getEmp_email() {
        return Emp_Email;
    }

    public void setEmp_email(String Emp_Email) {
        this.Emp_Email = Emp_Email;
    }


}