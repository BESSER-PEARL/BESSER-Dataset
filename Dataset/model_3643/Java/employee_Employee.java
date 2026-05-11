





import java.util.List;
import java.util.ArrayList;

public class employee_Employee  {

    private int empID;
    private boolean isManager;
    private String name;





    private employee_Company employee_company;




    private employee_Employee employee_employee;




    private employee_Employee employee_employee;




    private employee_Company employee_company;


    public employee_Employee(
        int empID,        boolean isManager,        String name    ) {
        this.empID = empID;
        this.isManager = isManager;
        this.name = name;
    }


    public int getEmpid() {
        return empID;
    }

    public void setEmpid(int empID) {
        this.empID = empID;
    }
    public boolean getIsmanager() {
        return isManager;
    }

    public void setIsmanager(boolean isManager) {
        this.isManager = isManager;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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