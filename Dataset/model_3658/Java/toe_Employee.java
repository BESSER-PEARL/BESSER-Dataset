





import java.util.List;
import java.util.ArrayList;

public class toe_Employee extends AllBase {

    private String name;
    private int salary;



    public toe_Employee(
        String name,        int salary    ) {
        super(
        );
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