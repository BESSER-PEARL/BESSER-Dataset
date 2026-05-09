





import java.util.List;
import java.util.ArrayList;

public class Families_Member  {

    private String firstName;





    private List<Person> persons;


    public Families_Member(
        String firstName    ) {
        this.firstName = firstName;
        this.persons = new ArrayList<>();
    }

    public Families_Member(
        String firstName        ArrayList<Person> persons    ) {
        this.firstName = firstName;
        this.persons = persons;
    }

    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
        this.firstName = firstName;
    }

    public List<Person> getPersons() {
        return persons;
    }

    public void addPerson(Person person) {
        this.persons.add(person);
    }

}