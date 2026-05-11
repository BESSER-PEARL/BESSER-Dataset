





import java.util.List;
import java.util.ArrayList;

public class employee_Department extends NamedEntity {






    private employee_Company employee_company;




    private List<employee_Employee> employee_employees;


    public employee_Department(
    ) {
        super(
        );
        this.employee_employees = new ArrayList<>();
    }

    public employee_Department(
        ArrayList<employee_Employee> employee_employees    ) {
        this.employee_employees = employee_employees;
    }


    public employee_Company getEmployee_company() {
        return employee_company;
    }

    public void setEmployee_company(employee_Company employee_company) {
        this.employee_company = employee_company;
    }
    public List<employee_Employee> getEmployee_employees() {
        return employee_employees;
    }

    public void addEmployee_employee(Employee_employee employee_employee) {
        this.employee_employees.add(employee_employee);
    }

}