





import java.util.List;
import java.util.ArrayList;

public class EvoCompany_Organisation  {

    private String name;
    private String city;
    private String completeAddress;





    private List<EvoCompany_Project> evocompany_projects;




    private List<EvoCompany_Person> evocompany_persons;


    public EvoCompany_Organisation(
        String name,        String city,        String completeAddress    ) {
        this.name = name;
        this.city = city;
        this.completeAddress = completeAddress;
        this.evocompany_projects = new ArrayList<>();
        this.evocompany_persons = new ArrayList<>();
    }

    public EvoCompany_Organisation(
        String name,        String city,        String completeAddress        ArrayList<EvoCompany_Project> evocompany_projects,        ArrayList<EvoCompany_Person> evocompany_persons    ) {
        this.name = name;
        this.city = city;
        this.completeAddress = completeAddress;
        this.evocompany_projects = evocompany_projects;
        this.evocompany_persons = evocompany_persons;
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

    public List<EvoCompany_Project> getEvocompany_projects() {
        return evocompany_projects;
    }

    public void addEvocompany_project(Evocompany_project evocompany_project) {
        this.evocompany_projects.add(evocompany_project);
    }
    public List<EvoCompany_Person> getEvocompany_persons() {
        return evocompany_persons;
    }

    public void addEvocompany_person(Evocompany_person evocompany_person) {
        this.evocompany_persons.add(evocompany_person);
    }

}