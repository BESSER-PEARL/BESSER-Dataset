





import java.util.List;
import java.util.ArrayList;

public class company_Department  {

    private String name;
    private int budget;





    private company_Company company_company;


    public company_Department(
        String name,        int budget    ) {
        this.name = name;
        this.budget = budget;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getBudget() {
        return budget;
    }

    public void setBudget(int budget) {
        this.budget = budget;
    }

    public company_Company getCompany_company() {
        return company_company;
    }

    public void setCompany_company(company_Company company_company) {
        this.company_company = company_company;
    }

}