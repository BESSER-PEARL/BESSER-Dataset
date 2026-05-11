





import java.util.List;
import java.util.ArrayList;

public class company_Employee  {

    private String name;
    private boolean hasNameAsAttribute;





    private List<company_Employee> company_employees;




    private company_Employee company_employee;




    private company_Company company_company;




    private company_Employee company_employee;




    private company_Employee company_employee;




    private company_Company company_company;


    public company_Employee(
        String name,        boolean hasNameAsAttribute    ) {
        this.name = name;
        this.hasNameAsAttribute = hasNameAsAttribute;
        this.company_employees = new ArrayList<>();
    }

    public company_Employee(
        String name,        boolean hasNameAsAttribute        ArrayList<company_Employee> company_employees    ) {
        this.name = name;
        this.hasNameAsAttribute = hasNameAsAttribute;
        this.company_employees = company_employees;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getHasnameasattribute() {
        return hasNameAsAttribute;
    }

    public void setHasnameasattribute(boolean hasNameAsAttribute) {
        this.hasNameAsAttribute = hasNameAsAttribute;
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
    public company_Company getCompany_company() {
        return company_company;
    }

    public void setCompany_company(company_Company company_company) {
        this.company_company = company_company;
    }
    public company_Employee getCompany_employee() {
        return company_employee;
    }

    public void setCompany_employee(company_Employee company_employee) {
        this.company_employee = company_employee;
    }
    public company_Employee getCompany_employee() {
        return company_employee;
    }

    public void setCompany_employee(company_Employee company_employee) {
        this.company_employee = company_employee;
    }
    public company_Company getCompany_company() {
        return company_company;
    }

    public void setCompany_company(company_Company company_company) {
        this.company_company = company_company;
    }

}