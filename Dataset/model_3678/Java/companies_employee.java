





import java.util.List;
import java.util.ArrayList;

public class companies_employee extends CSTrace {

    private float salary;
    private String address;
    private String mentor;
    private String name;





    private companies_department_employees companies_department_employees;




    private companies_department_manager companies_department_manager;


    public companies_employee(
        float salary,        String address,        String mentor,        String name    ) {
        super(
        );
        this.salary = salary;
        this.address = address;
        this.mentor = mentor;
        this.name = name;
    }


    public float getSalary() {
        return salary;
    }

    public void setSalary(float salary) {
        this.salary = salary;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getMentor() {
        return mentor;
    }

    public void setMentor(String mentor) {
        this.mentor = mentor;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public companies_department_employees getCompanies_department_employees() {
        return companies_department_employees;
    }

    public void setCompanies_department_employees(companies_department_employees companies_department_employees) {
        this.companies_department_employees = companies_department_employees;
    }
    public companies_department_manager getCompanies_department_manager() {
        return companies_department_manager;
    }

    public void setCompanies_department_manager(companies_department_manager companies_department_manager) {
        this.companies_department_manager = companies_department_manager;
    }

}