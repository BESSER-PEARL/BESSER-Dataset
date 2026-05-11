





import java.util.List;
import java.util.ArrayList;

public class company_Department extends NamedElement {

    private int numberOfEmployees;
    private int ageSumOfEmployees;





    private company_Company company_company;


    public company_Department(
        int numberOfEmployees,        int ageSumOfEmployees    ) {
        super(
        );
        this.numberOfEmployees = numberOfEmployees;
        this.ageSumOfEmployees = ageSumOfEmployees;
    }


    public int getNumberofemployees() {
        return numberOfEmployees;
    }

    public void setNumberofemployees(int numberOfEmployees) {
        this.numberOfEmployees = numberOfEmployees;
    }
    public int getAgesumofemployees() {
        return ageSumOfEmployees;
    }

    public void setAgesumofemployees(int ageSumOfEmployees) {
        this.ageSumOfEmployees = ageSumOfEmployees;
    }

    public company_Company getCompany_company() {
        return company_company;
    }

    public void setCompany_company(company_Company company_company) {
        this.company_company = company_company;
    }

}