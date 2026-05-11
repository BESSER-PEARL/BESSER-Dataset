





import java.util.List;
import java.util.ArrayList;

public class Company_Category  {

    private String name;





    private Company_CompanyModel company_companymodel;




    private Company_Project company_project;


    public Company_Category(
        String name    ) {
        this.name = name;
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
    public Company_Project getCompany_project() {
        return company_project;
    }

    public void setCompany_project(Company_Project company_project) {
        this.company_project = company_project;
    }

}