





import java.util.List;
import java.util.ArrayList;

public class CarRental_Employee extends Person {

    private float salary;



    public CarRental_Employee(
        float salary    ) {
        super(
        );
        this.salary = salary;
    }


    public float getSalary() {
        return salary;
    }

    public void setSalary(float salary) {
        this.salary = salary;
    }


}