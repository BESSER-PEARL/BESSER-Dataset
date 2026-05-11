





import java.util.List;
import java.util.ArrayList;

public class CarRental2_Employee extends Person {

    private int salary;



    public CarRental2_Employee(
        int salary    ) {
        super(
        );
        this.salary = salary;
    }


    public int getSalary() {
        return salary;
    }

    public void setSalary(int salary) {
        this.salary = salary;
    }


}