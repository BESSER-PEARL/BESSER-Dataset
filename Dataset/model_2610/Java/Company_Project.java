





import java.util.List;
import java.util.ArrayList;

public class Company_Project  {

    private String name;





    private Company_Person company_person;




    private Company_Category company_category;




    private Company_Organisation company_organisation;


    public Company_Project(
        String name    ) {
        this.name = name;
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
    public Company_Category getCompany_category() {
        return company_category;
    }

    public void setCompany_category(Company_Category company_category) {
        this.company_category = company_category;
    }
    public Company_Organisation getCompany_organisation() {
        return company_organisation;
    }

    public void setCompany_organisation(Company_Organisation company_organisation) {
        this.company_organisation = company_organisation;
    }

}