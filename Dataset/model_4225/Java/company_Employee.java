





import java.util.List;
import java.util.ArrayList;

public class company_Employee  {

    private String name;
    private String address;
    private float salary;





    private company_Department company_department;




    private company_Department company_department;




    private company_Employee company_employee;


    public company_Employee(
        String name,        String address,        float salary    ) {
        this.name = name;
        this.address = address;
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
    public float getSalary() {
        return salary;
    }

    public void setSalary(float salary) {
        this.salary = salary;
    }

    public company_Department getCompany_department() {
        return company_department;
    }

    public void setCompany_department(company_Department company_department) {
        this.company_department = company_department;
    }
    public company_Department getCompany_department() {
        return company_department;
    }

    public void setCompany_department(company_Department company_department) {
        this.company_department = company_department;
    }
    public company_Employee getCompany_employee() {
        return company_employee;
    }

    public void setCompany_employee(company_Employee company_employee) {
        this.company_employee = company_employee;
    }

}