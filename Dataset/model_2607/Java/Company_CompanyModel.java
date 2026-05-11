





import java.util.List;
import java.util.ArrayList;

public class Company_CompanyModel  {






    private List<Company_Category> company_categorys;




    private List<Company_Topic> company_topics;


    public Company_CompanyModel(
    ) {
        this.company_categorys = new ArrayList<>();
        this.company_topics = new ArrayList<>();
    }

    public Company_CompanyModel(
        ArrayList<Company_Category> company_categorys,        ArrayList<Company_Topic> company_topics    ) {
        this.company_categorys = company_categorys;
        this.company_topics = company_topics;
    }


    public List<Company_Category> getCompany_categorys() {
        return company_categorys;
    }

    public void addCompany_category(Company_category company_category) {
        this.company_categorys.add(company_category);
    }
    public List<Company_Topic> getCompany_topics() {
        return company_topics;
    }

    public void addCompany_topic(Company_topic company_topic) {
        this.company_topics.add(company_topic);
    }

}