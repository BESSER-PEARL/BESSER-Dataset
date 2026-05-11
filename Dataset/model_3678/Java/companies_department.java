





import java.util.List;
import java.util.ArrayList;

public class companies_department extends CSTrace {

    private String name;





    private companies_department companies_department;




    private companies_department_employees companies_department_employees;




    private companies_company companies_company;




    private companies_department_manager companies_department_manager;


    public companies_department(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public companies_department getCompanies_department() {
        return companies_department;
    }

    public void setCompanies_department(companies_department companies_department) {
        this.companies_department = companies_department;
    }
    public companies_department_employees getCompanies_department_employees() {
        return companies_department_employees;
    }

    public void setCompanies_department_employees(companies_department_employees companies_department_employees) {
        this.companies_department_employees = companies_department_employees;
    }
    public companies_company getCompanies_company() {
        return companies_company;
    }

    public void setCompanies_company(companies_company companies_company) {
        this.companies_company = companies_company;
    }
    public companies_department_manager getCompanies_department_manager() {
        return companies_department_manager;
    }

    public void setCompanies_department_manager(companies_department_manager companies_department_manager) {
        this.companies_department_manager = companies_department_manager;
    }

}