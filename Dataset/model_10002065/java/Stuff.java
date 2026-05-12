





import java.util.List;
import java.util.ArrayList;

public class Stuff  {

    private String WorkHours;
    private String Salary;



    public Stuff(
        String WorkHours,        String Salary    ) {
        this.WorkHours = WorkHours;
        this.Salary = Salary;
    }


    public String getWorkhours() {
        return WorkHours;
    }

    public void setWorkhours(String WorkHours) {
        this.WorkHours = WorkHours;
    }
    public String getSalary() {
        return Salary;
    }

    public void setSalary(String Salary) {
        this.Salary = Salary;
    }


}