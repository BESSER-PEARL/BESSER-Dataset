





import java.util.List;
import java.util.ArrayList;

public class Company_CompanyModel  {






    private List<Company_Category> company_categorys;




    private List<Company_Company> company_companys;




    private List<Company_Division> company_divisions;




    private List<Company_Topic> company_topics;


    public Company_CompanyModel(
    ) {
        this.company_categorys = new ArrayList<>();
        this.company_companys = new ArrayList<>();
        this.company_divisions = new ArrayList<>();
        this.company_topics = new ArrayList<>();
    }

    public Company_CompanyModel(
        ArrayList<Company_Category> company_categorys,        ArrayList<Company_Company> company_companys,        ArrayList<Company_Division> company_divisions,        ArrayList<Company_Topic> company_topics    ) {
        this.company_categorys = company_categorys;
        this.company_companys = company_companys;
        this.company_divisions = company_divisions;
        this.company_topics = company_topics;
    }


    public List<Company_Category> getCompany_categorys() {
        return company_categorys;
    }

    public void addCompany_category(Company_category company_category) {
        this.company_categorys.add(company_category);
    }
    public List<Company_Company> getCompany_companys() {
        return company_companys;
    }

    public void addCompany_company(Company_company company_company) {
        this.company_companys.add(company_company);
    }
    public List<Company_Division> getCompany_divisions() {
        return company_divisions;
    }

    public void addCompany_division(Company_division company_division) {
        this.company_divisions.add(company_division);
    }
    public List<Company_Topic> getCompany_topics() {
        return company_topics;
    }

    public void addCompany_topic(Company_topic company_topic) {
        this.company_topics.add(company_topic);
    }

}