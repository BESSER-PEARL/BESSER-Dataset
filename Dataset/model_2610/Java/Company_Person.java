





import java.util.List;
import java.util.ArrayList;

public class Company_Person  {

    private String firstname;
    private String lastname;
    private String position;





    private Company_Organisation company_organisation;




    private Company_ServiceLine company_serviceline;


    public Company_Person(
        String firstname,        String lastname,        String position    ) {
        this.firstname = firstname;
        this.lastname = lastname;
        this.position = position;
    }


    public String getFirstname() {
        return firstname;
    }

    public void setFirstname(String firstname) {
        this.firstname = firstname;
    }
    public String getLastname() {
        return lastname;
    }

    public void setLastname(String lastname) {
        this.lastname = lastname;
    }
    public String getPosition() {
        return position;
    }

    public void setPosition(String position) {
        this.position = position;
    }

    public Company_Organisation getCompany_organisation() {
        return company_organisation;
    }

    public void setCompany_organisation(Company_Organisation company_organisation) {
        this.company_organisation = company_organisation;
    }
    public Company_ServiceLine getCompany_serviceline() {
        return company_serviceline;
    }

    public void setCompany_serviceline(Company_ServiceLine company_serviceline) {
        this.company_serviceline = company_serviceline;
    }

}