





import java.util.List;
import java.util.ArrayList;

public class Company_Company  {

    private String name;
    private String city;
    private String completeAddress;





    private List<Company_Person> company_persons;




    private List<Company_Project> company_projects;


    public Company_Company(
        String name,        String city,        String completeAddress    ) {
        this.name = name;
        this.city = city;
        this.completeAddress = completeAddress;
        this.company_persons = new ArrayList<>();
        this.company_projects = new ArrayList<>();
    }

    public Company_Company(
        String name,        String city,        String completeAddress        ArrayList<Company_Person> company_persons,        ArrayList<Company_Project> company_projects    ) {
        this.name = name;
        this.city = city;
        this.completeAddress = completeAddress;
        this.company_persons = company_persons;
        this.company_projects = company_projects;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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

}