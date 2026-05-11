





import java.util.List;
import java.util.ArrayList;

public class Company_Project  {

    private int budget;
    private String name;





    private Company_Person company_person;


    public Company_Project(
        int budget,        String name    ) {
        this.budget = budget;
        this.name = name;
    }


    public int getBudget() {
        return budget;
    }

    public void setBudget(int budget) {
        this.budget = budget;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Company_Person getCompany_person() {
        return company_person;
    }

    public void setCompany_person(Company_Person company_person) {
        this.company_person = company_person;
    }

}