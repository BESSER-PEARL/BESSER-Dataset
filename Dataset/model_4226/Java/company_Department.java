





import java.util.List;
import java.util.ArrayList;

public class company_Department extends Visitable {

    private String name;





    private List<company_Employee> company_employees;




    private company_Employee company_employee;




    private List<company_Department> company_departments;




    private company_Company company_company;


    public company_Department(
        String name    ) {
        super(
        );
        this.name = name;
        this.company_employees = new ArrayList<>();
        this.company_departments = new ArrayList<>();
    }

    public company_Department(
        String name        ArrayList<company_Employee> company_employees,        ArrayList<company_Department> company_departments    ) {
        this.name = name;
        this.company_employees = company_employees;
        this.company_departments = company_departments;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<company_Employee> getCompany_employees() {
        return company_employees;
    }

    public void addCompany_employee(Company_employee company_employee) {
        this.company_employees.add(company_employee);
    }
    public company_Employee getCompany_employee() {
        return company_employee;
    }

    public void setCompany_employee(company_Employee company_employee) {
        this.company_employee = company_employee;
    }
    public List<company_Department> getCompany_departments() {
        return company_departments;
    }

    public void addCompany_department(Company_department company_department) {
        this.company_departments.add(company_department);
    }
    public company_Company getCompany_company() {
        return company_company;
    }

    public void setCompany_company(company_Company company_company) {
        this.company_company = company_company;
    }

}