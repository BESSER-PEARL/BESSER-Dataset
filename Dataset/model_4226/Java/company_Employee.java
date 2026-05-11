





import java.util.List;
import java.util.ArrayList;

public class company_Employee extends Visitable {

    private float salary;
    private String name;
    private String address;





    private company_Employee company_employee;


    public company_Employee(
        float salary,        String name,        String address    ) {
        super(
        );
        this.salary = salary;
        this.name = name;
        this.address = address;
    }


    public float getSalary() {
        return salary;
    }

    public void setSalary(float salary) {
        this.salary = salary;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public company_Employee getCompany_employee() {
        return company_employee;
    }

    public void setCompany_employee(company_Employee company_employee) {
        this.company_employee = company_employee;
    }

}