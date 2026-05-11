





import java.util.List;
import java.util.ArrayList;

public class bz321765_Employee  {

    private String title;
    private String salary;



    public bz321765_Employee(
        String title,        String salary    ) {
        this.title = title;
        this.salary = salary;
    }


    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getSalary() {
        return salary;
    }

    public void setSalary(String salary) {
        this.salary = salary;
    }


}