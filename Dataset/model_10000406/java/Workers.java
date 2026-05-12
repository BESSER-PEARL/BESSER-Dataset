





import java.util.List;
import java.util.ArrayList;

public class Workers  {

    private String name;
    private String Password;
    private String Designation;
    private int salary;



    public Workers(
        String name,        String Password,        String Designation,        int salary    ) {
        this.name = name;
        this.Password = Password;
        this.Designation = Designation;
        this.salary = salary;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }
    public String getDesignation() {
        return Designation;
    }

    public void setDesignation(String Designation) {
        this.Designation = Designation;
    }
    public int getSalary() {
        return salary;
    }

    public void setSalary(int salary) {
        this.salary = salary;
    }


}