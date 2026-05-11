





import java.util.List;
import java.util.ArrayList;

public class Company_Division  {

    private String name;





    private Company_Organisation company_organisation;


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

    public Company_Organisation getCompany_organisation() {
        return company_organisation;
    }

    public void setCompany_organisation(Company_Organisation company_organisation) {
        this.company_organisation = company_organisation;
    }

}