





import java.util.List;
import java.util.ArrayList;

public class Company_Project  {

    private String name;
    private int budget;





    private Company_Topic company_topic;




    private Company_Person company_person;


    public Company_Project(
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

    public Company_Topic getCompany_topic() {
        return company_topic;
    }

    public void setCompany_topic(Company_Topic company_topic) {
        this.company_topic = company_topic;
    }
    public Company_Person getCompany_person() {
        return company_person;
    }

    public void setCompany_person(Company_Person company_person) {
        this.company_person = company_person;
    }

}