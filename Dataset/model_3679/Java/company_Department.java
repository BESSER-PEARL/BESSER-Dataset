





import java.util.List;
import java.util.ArrayList;

public class company_Department  {

    private int number;





    private company_Employee company_employee;




    private List<company_Employee> company_employees;


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

    public company_Employee getCompany_employee() {
        return company_employee;
    }

    public void setCompany_employee(company_Employee company_employee) {
        this.company_employee = company_employee;
    }
    public List<company_Employee> getCompany_employees() {
        return company_employees;
    }

    public void addCompany_employee(Company_employee company_employee) {
        this.company_employees.add(company_employee);
    }

}