





import java.util.List;
import java.util.ArrayList;

public class Company_Project  {

    private int budget;
    private String name;





    private Company_Person company_person;




    private Company_Topic company_topic;




    private Company_Organisation company_organisation;


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
    public Company_Topic getCompany_topic() {
        return company_topic;
    }

    public void setCompany_topic(Company_Topic company_topic) {
        this.company_topic = company_topic;
    }
    public Company_Organisation getCompany_organisation() {
        return company_organisation;
    }

    public void setCompany_organisation(Company_Organisation company_organisation) {
        this.company_organisation = company_organisation;
    }

}