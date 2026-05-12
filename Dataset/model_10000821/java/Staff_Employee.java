





import java.util.List;
import java.util.ArrayList;

public class Staff_Employee  {

    private String name;
    private float salary;
    private String nationalInsurance;



    public Staff_Employee(
        String name,        float salary,        String nationalInsurance    ) {
        this.name = name;
        this.salary = salary;
        this.nationalInsurance = nationalInsurance;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public float getSalary() {
        return salary;
    }

    public void setSalary(float salary) {
        this.salary = salary;
    }
    public String getNationalinsurance() {
        return nationalInsurance;
    }

    public void setNationalinsurance(String nationalInsurance) {
        this.nationalInsurance = nationalInsurance;
    }


}