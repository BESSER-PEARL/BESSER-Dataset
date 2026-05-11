





import java.util.List;
import java.util.ArrayList;

public class Company_Department  {

    private int budget;
    private String name;
    private String location;





    private Company_Employee company_employee;




    private List<Company_Employee> company_employees;


    public Company_Department(
        int budget,        String name,        String location    ) {
        this.budget = budget;
        this.name = name;
        this.location = location;
        this.company_employees = new ArrayList<>();
    }

    public Company_Department(
        int budget,        String name,        String location        ArrayList<Company_Employee> company_employees    ) {
        this.budget = budget;
        this.name = name;
        this.location = location;
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
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }

    public Company_Employee getCompany_employee() {
        return company_employee;
    }

    public void setCompany_employee(Company_Employee company_employee) {
        this.company_employee = company_employee;
    }
    public List<Company_Employee> getCompany_employees() {
        return company_employees;
    }

    public void addCompany_employee(Company_employee company_employee) {
        this.company_employees.add(company_employee);
    }

}