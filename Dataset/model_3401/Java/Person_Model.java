





import java.util.List;
import java.util.ArrayList;

public class Person_Model  {






    private List<Person_Person> person_persons;


    public Person_Model(
    ) {
        this.person_persons = new ArrayList<>();
    }

    public Person_Model(
        ArrayList<Person_Person> person_persons    ) {
        this.person_persons = person_persons;
    }


    public List<Person_Person> getPerson_persons() {
        return person_persons;
    }

    public void addPerson_person(Person_person person_person) {
        this.person_persons.add(person_person);
    }

}