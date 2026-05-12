





import java.util.List;
import java.util.ArrayList;

public class Employee  {

    private String Emp_FName;
    private String Emp_Id;
    private String Emp_Name;



    public Employee(
        String Emp_FName,        String Emp_Id,        String Emp_Name    ) {
        this.Emp_FName = Emp_FName;
        this.Emp_Id = Emp_Id;
        this.Emp_Name = Emp_Name;
    }


    public String getEmp_fname() {
        return Emp_FName;
    }

    public void setEmp_fname(String Emp_FName) {
        this.Emp_FName = Emp_FName;
    }
    public String getEmp_id() {
        return Emp_Id;
    }

    public void setEmp_id(String Emp_Id) {
        this.Emp_Id = Emp_Id;
    }
    public String getEmp_name() {
        return Emp_Name;
    }

    public void setEmp_name(String Emp_Name) {
        this.Emp_Name = Emp_Name;
    }


}