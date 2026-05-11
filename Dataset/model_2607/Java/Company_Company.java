





import java.util.List;
import java.util.ArrayList;

public class Company_Company  {

    private String name;





    private List<Company_Person> company_persons;




    private List<Company_Project> company_projects;




    private Company_CompanyModel company_companymodel;


    public Company_Company(
        String name    ) {
        this.name = name;
        this.company_persons = new ArrayList<>();
        this.company_projects = new ArrayList<>();
    }

    public Company_Company(
        String name        ArrayList<Company_Person> company_persons,        ArrayList<Company_Project> company_projects    ) {
        this.name = name;
        this.company_persons = company_persons;
        this.company_projects = company_projects;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<Company_Person> getCompany_persons() {
        return company_persons;
    }

    public void addCompany_person(Company_person company_person) {
        this.company_persons.add(company_person);
    }
    public List<Company_Project> getCompany_projects() {
        return company_projects;
    }

    public void addCompany_project(Company_project company_project) {
        this.company_projects.add(company_project);
    }
    public Company_CompanyModel getCompany_companymodel() {
        return company_companymodel;
    }

    public void setCompany_companymodel(Company_CompanyModel company_companymodel) {
        this.company_companymodel = company_companymodel;
    }

}