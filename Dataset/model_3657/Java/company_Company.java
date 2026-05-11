





import java.util.List;
import java.util.ArrayList;

public class company_Company  {

    private String eotmDelta;
    private String name;





    private company_Division company_division;




    private company_Employee company_employee;




    private company_Division company_division;


    public company_Company(
        String eotmDelta,        String name    ) {
        this.eotmDelta = eotmDelta;
        this.name = name;
    }


    public String getEotmdelta() {
        return eotmDelta;
    }

    public void setEotmdelta(String eotmDelta) {
        this.eotmDelta = eotmDelta;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public company_Division getCompany_division() {
        return company_division;
    }

    public void setCompany_division(company_Division company_division) {
        this.company_division = company_division;
    }
    public company_Employee getCompany_employee() {
        return company_employee;
    }

    public void setCompany_employee(company_Employee company_employee) {
        this.company_employee = company_employee;
    }
    public company_Division getCompany_division() {
        return company_division;
    }

    public void setCompany_division(company_Division company_division) {
        this.company_division = company_division;
    }

}