





import java.util.List;
import java.util.ArrayList;

public class company_Company  {

    private String size;
    private String name;





    private List<company_Employee> company_employees;




    private company_Employee company_employee;


    public company_Company(
        String size,        String name    ) {
        this.size = size;
        this.name = name;
        this.company_employees = new ArrayList<>();
    }

    public company_Company(
        String size,        String name        ArrayList<company_Employee> company_employees    ) {
        this.size = size;
        this.name = name;
        this.company_employees = company_employees;
    }

    public String getSize() {
        return size;
    }

    public void setSize(String size) {
        this.size = size;
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

}