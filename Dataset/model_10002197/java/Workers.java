





import java.util.List;
import java.util.ArrayList;

public class Workers  {

    private String Designation;
    private String Password;
    private String name;
    private int salary;



    public Workers(
        String Designation,        String Password,        String name,        int salary    ) {
        this.Designation = Designation;
        this.Password = Password;
        this.name = name;
        this.salary = salary;
    }


    public String getDesignation() {
        return Designation;
    }

    public void setDesignation(String Designation) {
        this.Designation = Designation;
    }
    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getSalary() {
        return salary;
    }

    public void setSalary(int salary) {
        this.salary = salary;
    }


}