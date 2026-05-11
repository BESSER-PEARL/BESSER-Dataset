





import java.util.List;
import java.util.ArrayList;

public class company_Department  {

    private int number;





    private List<company_Employee> company_employees;




    private company_Company company_company;


    public company_Department(
        int number    ) {
        this.number = number;
        this.company_employees = new ArrayList<>();
    }

    public company_Department(
        int number        ArrayList<company_Employee> company_employees    ) {
        this.number = number;
        this.company_employees = company_employees;
    }

    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }

    public List<company_Employee> getCompany_employees() {
        return company_employees;
    }

    public void addCompany_employee(Company_employee company_employee) {
        this.company_employees.add(company_employee);
    }
    public company_Company getCompany_company() {
        return company_company;
    }

    public void setCompany_company(company_Company company_company) {
        this.company_company = company_company;
    }

}