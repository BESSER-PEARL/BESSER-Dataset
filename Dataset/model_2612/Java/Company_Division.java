





import java.util.List;
import java.util.ArrayList;

public class Company_Division  {

    private String name;





    private Company_Company company_company;




    private Company_CompanyModel company_companymodel;


    public Company_Division(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Company_Company getCompany_company() {
        return company_company;
    }

    public void setCompany_company(Company_Company company_company) {
        this.company_company = company_company;
    }
    public Company_CompanyModel getCompany_companymodel() {
        return company_companymodel;
    }

    public void setCompany_companymodel(Company_CompanyModel company_companymodel) {
        this.company_companymodel = company_companymodel;
    }

}