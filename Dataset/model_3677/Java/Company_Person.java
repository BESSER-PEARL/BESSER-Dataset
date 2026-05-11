





import java.util.List;
import java.util.ArrayList;

public class Company_Person  {

    private String fullName;





    private Company_Organisation company_organisation;


    public Company_Person(
        String fullName    ) {
        this.fullName = fullName;
    }


    public String getFullname() {
        return fullName;
    }

    public void setFullname(String fullName) {
        this.fullName = fullName;
    }

    public Company_Organisation getCompany_organisation() {
        return company_organisation;
    }

    public void setCompany_organisation(Company_Organisation company_organisation) {
        this.company_organisation = company_organisation;
    }

}