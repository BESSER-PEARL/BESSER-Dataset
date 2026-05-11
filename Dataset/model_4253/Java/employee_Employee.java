





import java.util.List;
import java.util.ArrayList;

public class employee_Employee  {

    private String name;
    private String accounts;





    private employee_Employee employee_employee;




    private employee_Employee employee_employee;




    private List<employee_Employee> employee_employees;


    public employee_Employee(
        String name,        String accounts    ) {
        this.name = name;
        this.accounts = accounts;
        this.employee_employees = new ArrayList<>();
    }

    public employee_Employee(
        String name,        String accounts        ArrayList<employee_Employee> employee_employees    ) {
        this.name = name;
        this.accounts = accounts;
        this.employee_employees = employee_employees;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAccounts() {
        return accounts;
    }

    public void setAccounts(String accounts) {
        this.accounts = accounts;
    }

    public employee_Employee getEmployee_employee() {
        return employee_employee;
    }

    public void setEmployee_employee(employee_Employee employee_employee) {
        this.employee_employee = employee_employee;
    }
    public employee_Employee getEmployee_employee() {
        return employee_employee;
    }

    public void setEmployee_employee(employee_Employee employee_employee) {
        this.employee_employee = employee_employee;
    }
    public List<employee_Employee> getEmployee_employees() {
        return employee_employees;
    }

    public void addEmployee_employee(Employee_employee employee_employee) {
        this.employee_employees.add(employee_employee);
    }

}