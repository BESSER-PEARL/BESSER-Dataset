





import java.util.List;
import java.util.ArrayList;

public class Company_Address  {

    private String completeAddress;
    private String city;





    private Company_Company company_company;




    private Company_CompanyModel company_companymodel;


    public Company_Address(
        String completeAddress,        String city    ) {
        this.completeAddress = completeAddress;
        this.city = city;
    }


    public String getCompleteaddress() {
        return completeAddress;
    }

    public void setCompleteaddress(String completeAddress) {
        this.completeAddress = completeAddress;
    }
    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
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