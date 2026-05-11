





import java.util.List;
import java.util.ArrayList;

public class CompanyModel_Department  {

    private int number;





    private CompanyModel_Company companymodel_company;


    public CompanyModel_Department(
        int number    ) {
        this.number = number;
    }


    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }

    public CompanyModel_Company getCompanymodel_company() {
        return companymodel_company;
    }

    public void setCompanymodel_company(CompanyModel_Company companymodel_company) {
        this.companymodel_company = companymodel_company;
    }

}