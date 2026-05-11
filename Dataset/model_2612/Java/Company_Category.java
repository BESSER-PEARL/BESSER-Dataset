





import java.util.List;
import java.util.ArrayList;

public class Company_Category  {

    private String name;





    private Company_CompanyModel company_companymodel;




    private Company_Topic company_topic;




    private List<Company_Topic> company_topics;




    private Company_Project company_project;


    public Company_Category(
        String name    ) {
        this.name = name;
        this.company_topics = new ArrayList<>();
    }

    public Company_Category(
        String name        ArrayList<Company_Topic> company_topics    ) {
        this.name = name;
        this.company_topics = company_topics;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Company_CompanyModel getCompany_companymodel() {
        return company_companymodel;
    }

    public void setCompany_companymodel(Company_CompanyModel company_companymodel) {
        this.company_companymodel = company_companymodel;
    }
    public Company_Topic getCompany_topic() {
        return company_topic;
    }

    public void setCompany_topic(Company_Topic company_topic) {
        this.company_topic = company_topic;
    }
    public List<Company_Topic> getCompany_topics() {
        return company_topics;
    }

    public void addCompany_topic(Company_topic company_topic) {
        this.company_topics.add(company_topic);
    }
    public Company_Project getCompany_project() {
        return company_project;
    }

    public void setCompany_project(Company_Project company_project) {
        this.company_project = company_project;
    }

}