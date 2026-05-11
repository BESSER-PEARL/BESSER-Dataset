





import java.util.List;
import java.util.ArrayList;

public class company_Category  {

    private String name;





    private List<company_Category> company_categorys;




    private company_Company company_company;


    public company_Category(
        String name    ) {
        this.name = name;
        this.company_categorys = new ArrayList<>();
    }

    public company_Category(
        String name        ArrayList<company_Category> company_categorys    ) {
        this.name = name;
        this.company_categorys = company_categorys;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<company_Category> getCompany_categorys() {
        return company_categorys;
    }

    public void addCompany_category(Company_category company_category) {
        this.company_categorys.add(company_category);
    }
    public company_Company getCompany_company() {
        return company_company;
    }

    public void setCompany_company(company_Company company_company) {
        this.company_company = company_company;
    }

}