





import java.util.List;
import java.util.ArrayList;

public class toe_Employee extends AllBase {

    private int salary;
    private String name;



    public toe_Employee(
        int salary,        String name    ) {
        super(
        );
        this.salary = salary;
        this.name = name;
    }


    public int getSalary() {
        return salary;
    }

    public void setSalary(int salary) {
        this.salary = salary;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}