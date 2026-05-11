





import java.util.List;
import java.util.ArrayList;

public class Company_Category  {

    private String name;





    private Company_Topic company_topic;




    private List<Company_Topic> company_topics;


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

}