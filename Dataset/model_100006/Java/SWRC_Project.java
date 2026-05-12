





import java.util.List;
import java.util.ArrayList;

public class SWRC_Project  {

    private String name;





    private List<Person> persons;




    private List<ResearchTopic> researchtopics;




    private AcademicStaff academicstaff;




    private Organization organization;




    private Organization organization;


    public SWRC_Project(
        String name    ) {
        this.name = name;
        this.persons = new ArrayList<>();
        this.researchtopics = new ArrayList<>();
    }

    public SWRC_Project(
        String name        ArrayList<Person> persons,        ArrayList<ResearchTopic> researchtopics    ) {
        this.name = name;
        this.persons = persons;
        this.researchtopics = researchtopics;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<Person> getPersons() {
        return persons;
    }

    public void addPerson(Person person) {
        this.persons.add(person);
    }
    public List<ResearchTopic> getResearchtopics() {
        return researchtopics;
    }

    public void addResearchtopic(Researchtopic researchtopic) {
        this.researchtopics.add(researchtopic);
    }
    public AcademicStaff getAcademicstaff() {
        return academicstaff;
    }

    public void setAcademicstaff(AcademicStaff academicstaff) {
        this.academicstaff = academicstaff;
    }
    public Organization getOrganization() {
        return organization;
    }

    public void setOrganization(Organization organization) {
        this.organization = organization;
    }
    public Organization getOrganization() {
        return organization;
    }

    public void setOrganization(Organization organization) {
        this.organization = organization;
    }

}