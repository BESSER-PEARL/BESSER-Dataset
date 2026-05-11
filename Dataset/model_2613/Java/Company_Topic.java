





import java.util.List;
import java.util.ArrayList;

public class Company_Topic  {

    private String id;





    private Company_Category company_category;




    private Company_CompanyModel company_companymodel;




    private Company_Category company_category;


    public Company_Topic(
        String id    ) {
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public Company_Category getCompany_category() {
        return company_category;
    }

    public void setCompany_category(Company_Category company_category) {
        this.company_category = company_category;
    }
    public Company_CompanyModel getCompany_companymodel() {
        return company_companymodel;
    }

    public void setCompany_companymodel(Company_CompanyModel company_companymodel) {
        this.company_companymodel = company_companymodel;
    }
    public Company_Category getCompany_category() {
        return company_category;
    }

    public void setCompany_category(Company_Category company_category) {
        this.company_category = company_category;
    }

}