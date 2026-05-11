





import java.util.List;
import java.util.ArrayList;

public class employee_Department  {

    private String name;
    private int deptID;





    private employee_Company employee_company;




    private employee_Employee employee_employee;




    private List<employee_Employee> employee_employees;




    private employee_Employee employee_employee;




    private employee_Company employee_company;


    public employee_Department(
        String name,        int deptID    ) {
        this.name = name;
        this.deptID = deptID;
        this.employee_employees = new ArrayList<>();
    }

    public employee_Department(
        String name,        int deptID        ArrayList<employee_Employee> employee_employees    ) {
        this.name = name;
        this.deptID = deptID;
        this.employee_employees = employee_employees;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getDeptid() {
        return deptID;
    }

    public void setDeptid(int deptID) {
        this.deptID = deptID;
    }

    public employee_Company getEmployee_company() {
        return employee_company;
    }

    public void setEmployee_company(employee_Company employee_company) {
        this.employee_company = employee_company;
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
    public employee_Employee getEmployee_employee() {
        return employee_employee;
    }

    public void setEmployee_employee(employee_Employee employee_employee) {
        this.employee_employee = employee_employee;
    }
    public employee_Company getEmployee_company() {
        return employee_company;
    }

    public void setEmployee_company(employee_Company employee_company) {
        this.employee_company = employee_company;
    }

}