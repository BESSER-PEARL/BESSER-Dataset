





import java.util.List;
import java.util.ArrayList;

public class Company_Topic  {

    private String id;





    private Company_Project company_project;


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

    public Company_Project getCompany_project() {
        return company_project;
    }

    public void setCompany_project(Company_Project company_project) {
        this.company_project = company_project;
    }

}