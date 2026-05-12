




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class staff_member  {

    private LocalDate staff_DOB;
    private String staff_NIC;
    private String staff_Department;
    private String staff_ContactNo;
    private String staff_Position;
    private String staff_Name;
    private int staff_Id;
    private LocalDate staff_Date_Of_Joint;
    private String staff_Email;
    private String staff_Address;
    private float staff_Salary;



    public staff_member(
        LocalDate staff_DOB,        String staff_NIC,        String staff_Department,        String staff_ContactNo,        String staff_Position,        String staff_Name,        int staff_Id,        LocalDate staff_Date_Of_Joint,        String staff_Email,        String staff_Address,        float staff_Salary    ) {
        this.staff_DOB = staff_DOB;
        this.staff_NIC = staff_NIC;
        this.staff_Department = staff_Department;
        this.staff_ContactNo = staff_ContactNo;
        this.staff_Position = staff_Position;
        this.staff_Name = staff_Name;
        this.staff_Id = staff_Id;
        this.staff_Date_Of_Joint = staff_Date_Of_Joint;
        this.staff_Email = staff_Email;
        this.staff_Address = staff_Address;
        this.staff_Salary = staff_Salary;
    }


    public LocalDate getStaff_dob() {
        return staff_DOB;
    }

    public void setStaff_dob(LocalDate staff_DOB) {
        this.staff_DOB = staff_DOB;
    }
    public String getStaff_nic() {
        return staff_NIC;
    }

    public void setStaff_nic(String staff_NIC) {
        this.staff_NIC = staff_NIC;
    }
    public String getStaff_department() {
        return staff_Department;
    }

    public void setStaff_department(String staff_Department) {
        this.staff_Department = staff_Department;
    }
    public String getStaff_contactno() {
        return staff_ContactNo;
    }

    public void setStaff_contactno(String staff_ContactNo) {
        this.staff_ContactNo = staff_ContactNo;
    }
    public String getStaff_position() {
        return staff_Position;
    }

    public void setStaff_position(String staff_Position) {
        this.staff_Position = staff_Position;
    }
    public String getStaff_name() {
        return staff_Name;
    }

    public void setStaff_name(String staff_Name) {
        this.staff_Name = staff_Name;
    }
    public int getStaff_id() {
        return staff_Id;
    }

    public void setStaff_id(int staff_Id) {
        this.staff_Id = staff_Id;
    }
    public LocalDate getStaff_date_of_joint() {
        return staff_Date_Of_Joint;
    }

    public void setStaff_date_of_joint(LocalDate staff_Date_Of_Joint) {
        this.staff_Date_Of_Joint = staff_Date_Of_Joint;
    }
    public String getStaff_email() {
        return staff_Email;
    }

    public void setStaff_email(String staff_Email) {
        this.staff_Email = staff_Email;
    }
    public String getStaff_address() {
        return staff_Address;
    }

    public void setStaff_address(String staff_Address) {
        this.staff_Address = staff_Address;
    }
    public float getStaff_salary() {
        return staff_Salary;
    }

    public void setStaff_salary(float staff_Salary) {
        this.staff_Salary = staff_Salary;
    }


}