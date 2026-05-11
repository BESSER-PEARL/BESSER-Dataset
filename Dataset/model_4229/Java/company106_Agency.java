





import java.util.List;
import java.util.ArrayList;

public class company106_Agency extends Function {

    private String status;
    private String acronym;





    private company106_Company company106_company;




    private List<company106_Employee> company106_employees;


    public company106_Agency(
        String status,        String acronym    ) {
        super(
        );
        this.status = status;
        this.acronym = acronym;
        this.company106_employees = new ArrayList<>();
    }

    public company106_Agency(
        String status,        String acronym        ArrayList<company106_Employee> company106_employees    ) {
        this.status = status;
        this.acronym = acronym;
        this.company106_employees = company106_employees;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public String getAcronym() {
        return acronym;
    }

    public void setAcronym(String acronym) {
        this.acronym = acronym;
    }

    public company106_Company getCompany106_company() {
        return company106_company;
    }

    public void setCompany106_company(company106_Company company106_company) {
        this.company106_company = company106_company;
    }
    public List<company106_Employee> getCompany106_employees() {
        return company106_employees;
    }

    public void addCompany106_employee(Company106_employee company106_employee) {
        this.company106_employees.add(company106_employee);
    }

}