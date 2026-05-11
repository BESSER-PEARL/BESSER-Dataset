





import java.util.List;
import java.util.ArrayList;

public class Company_Organisation  {

    private String city;
    private String completeAddress;
    private String name;





    private Company_CompanyModel company_companymodel;




    private List<Company_Division> company_divisions;




    private List<Company_Project> company_projects;




    private List<Company_Person> company_persons;


    public Company_Organisation(
        String city,        String completeAddress,        String name    ) {
        this.city = city;
        this.completeAddress = completeAddress;
        this.name = name;
        this.company_divisions = new ArrayList<>();
        this.company_projects = new ArrayList<>();
        this.company_persons = new ArrayList<>();
    }

    public Company_Organisation(
        String city,        String completeAddress,        String name        ArrayList<Company_Division> company_divisions,        ArrayList<Company_Project> company_projects,        ArrayList<Company_Person> company_persons    ) {
        this.city = city;
        this.completeAddress = completeAddress;
        this.name = name;
        this.company_divisions = company_divisions;
        this.company_projects = company_projects;
        this.company_persons = company_persons;
    }

    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }
    public String getCompleteaddress() {
        return completeAddress;
    }

    public void setCompleteaddress(String completeAddress) {
        this.completeAddress = completeAddress;
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
    public List<Company_Division> getCompany_divisions() {
        return company_divisions;
    }

    public void addCompany_division(Company_division company_division) {
        this.company_divisions.add(company_division);
    }
    public List<Company_Project> getCompany_projects() {
        return company_projects;
    }

    public void addCompany_project(Company_project company_project) {
        this.company_projects.add(company_project);
    }
    public List<Company_Person> getCompany_persons() {
        return company_persons;
    }

    public void addCompany_person(Company_person company_person) {
        this.company_persons.add(company_person);
    }

}