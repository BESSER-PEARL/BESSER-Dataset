





import java.util.List;
import java.util.ArrayList;

public class Company_Project  {

    private int budget;
    private String name;





    private Company_Department company_department;




    private Company_Department company_department;




    private List<Company_Employee> company_employees;




    private Company_Employee company_employee;


    public Company_Project(
        int budget,        String name    ) {
        this.budget = budget;
        this.name = name;
        this.company_employees = new ArrayList<>();
    }

    public Company_Project(
        int budget,        String name        ArrayList<Company_Employee> company_employees    ) {
        this.budget = budget;
        this.name = name;
        this.company_employees = company_employees;
    }

    public int getBudget() {
        return budget;
    }

    public void setBudget(int budget) {
        this.budget = budget;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Company_Department getCompany_department() {
        return company_department;
    }

    public void setCompany_department(Company_Department company_department) {
        this.company_department = company_department;
    }
    public Company_Department getCompany_department() {
        return company_department;
    }

    public void setCompany_department(Company_Department company_department) {
        this.company_department = company_department;
    }
    public List<Company_Employee> getCompany_employees() {
        return company_employees;
    }

    public void addCompany_employee(Company_employee company_employee) {
        this.company_employees.add(company_employee);
    }
    public Company_Employee getCompany_employee() {
        return company_employee;
    }

    public void setCompany_employee(Company_Employee company_employee) {
        this.company_employee = company_employee;
    }

}