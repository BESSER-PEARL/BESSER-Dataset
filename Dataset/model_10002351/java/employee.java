





import java.util.List;
import java.util.ArrayList;

public class employee  {

    private String id;
    private String password;
    private String department;
    private int Salary;



    public employee(
        String id,        String password,        String department,        int Salary    ) {
        this.id = id;
        this.password = password;
        this.department = department;
        this.Salary = Salary;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getDepartment() {
        return department;
    }

    public void setDepartment(String department) {
        this.department = department;
    }
    public int getSalary() {
        return Salary;
    }

    public void setSalary(int Salary) {
        this.Salary = Salary;
    }


}