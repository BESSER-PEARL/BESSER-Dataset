





import java.util.List;
import java.util.ArrayList;

public class Person_Person  {

    private String lastName;
    private String firstName;





    private List<Person_Person> person_persons;


    public Person_Person(
        String lastName,        String firstName    ) {
        this.lastName = lastName;
        this.firstName = firstName;
        this.person_persons = new ArrayList<>();
    }

    public Person_Person(
        String lastName,        String firstName        ArrayList<Person_Person> person_persons    ) {
        this.lastName = lastName;
        this.firstName = firstName;
        this.person_persons = person_persons;
    }

    public String getLastname() {
        return lastName;
    }

    public void setLastname(String lastName) {
        this.lastName = lastName;
    }
    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
        this.firstName = firstName;
    }

    public List<Person_Person> getPerson_persons() {
        return person_persons;
    }

    public void addPerson_person(Person_person person_person) {
        this.person_persons.add(person_person);
    }

}