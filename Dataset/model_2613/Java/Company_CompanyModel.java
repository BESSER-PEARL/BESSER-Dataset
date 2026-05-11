





import java.util.List;
import java.util.ArrayList;

public class Company_CompanyModel  {






    private List<Company_Company> company_companys;


    public Company_CompanyModel(
    ) {
        this.company_companys = new ArrayList<>();
    }

    public Company_CompanyModel(
        ArrayList<Company_Company> company_companys    ) {
        this.company_companys = company_companys;
    }


    public List<Company_Company> getCompany_companys() {
        return company_companys;
    }

    public void addCompany_company(Company_company company_company) {
        this.company_companys.add(company_company);
    }

}