





import java.util.List;
import java.util.ArrayList;

public class Company_CompanyModel  {






    private List<Company_Topic> company_topics;




    private List<Company_Category> company_categorys;




    private Company_Organisation company_organisation;




    private List<Company_Division> company_divisions;


    public Company_CompanyModel(
    ) {
        this.company_topics = new ArrayList<>();
        this.company_categorys = new ArrayList<>();
        this.company_divisions = new ArrayList<>();
    }

    public Company_CompanyModel(
        ArrayList<Company_Topic> company_topics,        ArrayList<Company_Category> company_categorys,        ArrayList<Company_Division> company_divisions    ) {
        this.company_topics = company_topics;
        this.company_categorys = company_categorys;
        this.company_divisions = company_divisions;
    }


    public List<Company_Topic> getCompany_topics() {
        return company_topics;
    }

    public void addCompany_topic(Company_topic company_topic) {
        this.company_topics.add(company_topic);
    }
    public List<Company_Category> getCompany_categorys() {
        return company_categorys;
    }

    public void addCompany_category(Company_category company_category) {
        this.company_categorys.add(company_category);
    }
    public Company_Organisation getCompany_organisation() {
        return company_organisation;
    }

    public void setCompany_organisation(Company_Organisation company_organisation) {
        this.company_organisation = company_organisation;
    }
    public List<Company_Division> getCompany_divisions() {
        return company_divisions;
    }

    public void addCompany_division(Company_division company_division) {
        this.company_divisions.add(company_division);
    }

}