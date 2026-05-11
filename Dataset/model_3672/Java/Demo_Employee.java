





import java.util.List;
import java.util.ArrayList;

public class Demo_Employee  {

    private boolean name;
    private int salary;



    public Demo_Employee(
        boolean name,        int salary    ) {
        this.name = name;
        this.salary = salary;
    }


    public boolean getName() {
        return name;
    }

    public void setName(boolean name) {
        this.name = name;
    }
    public int getSalary() {
        return salary;
    }

    public void setSalary(int salary) {
        this.salary = salary;
    }


}