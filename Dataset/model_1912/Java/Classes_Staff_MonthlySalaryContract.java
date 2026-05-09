





import java.util.List;
import java.util.ArrayList;

public class Classes_Staff_MonthlySalaryContract extends SalaryContract {

    private float salary;



    public Classes_Staff_MonthlySalaryContract(
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