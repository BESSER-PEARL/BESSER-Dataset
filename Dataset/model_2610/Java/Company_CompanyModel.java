





import java.util.List;
import java.util.ArrayList;

public class Company_CompanyModel  {






    private List<Company_Topic> company_topics;


    public Company_CompanyModel(
    ) {
        this.company_topics = new ArrayList<>();
    }

    public Company_CompanyModel(
        ArrayList<Company_Topic> company_topics    ) {
        this.company_topics = company_topics;
    }


    public List<Company_Topic> getCompany_topics() {
        return company_topics;
    }

    public void addCompany_topic(Company_topic company_topic) {
        this.company_topics.add(company_topic);
    }

}