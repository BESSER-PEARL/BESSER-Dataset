





import java.util.List;
import java.util.ArrayList;

public class Company_Employee  {

    private String name;
    private int salary;



    public Company_Employee(
        String name,        int salary    ) {
        this.name = name;
        this.salary = salary;
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