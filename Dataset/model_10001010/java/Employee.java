




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Employee  {

    private String Emp_Name;
    private int Emp_Id;
    private LocalDate Emp_DOB;
    private LocalDate Emp_Date_Of_Joint;
    private String Emp_Position;
    private String Emp_Address;



    public Employee(
        String Emp_Name,        int Emp_Id,        LocalDate Emp_DOB,        LocalDate Emp_Date_Of_Joint,        String Emp_Position,        String Emp_Address    ) {
        this.Emp_Name = Emp_Name;
        this.Emp_Id = Emp_Id;
        this.Emp_DOB = Emp_DOB;
        this.Emp_Date_Of_Joint = Emp_Date_Of_Joint;
        this.Emp_Position = Emp_Position;
        this.Emp_Address = Emp_Address;
    }


    public String getEmp_name() {
        return Emp_Name;
    }

    public void setEmp_name(String Emp_Name) {
        this.Emp_Name = Emp_Name;
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
    public String getEmp_address() {
        return Emp_Address;
    }

    public void setEmp_address(String Emp_Address) {
        this.Emp_Address = Emp_Address;
    }


}