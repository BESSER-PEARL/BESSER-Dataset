





import java.util.List;
import java.util.ArrayList;

public class Persons_PersonsModel  {






    private List<Person> persons;


    public Persons_PersonsModel(
    ) {
        this.persons = new ArrayList<>();
    }

    public Persons_PersonsModel(
        ArrayList<Person> persons    ) {
        this.persons = persons;
    }


    public List<Person> getPersons() {
        return persons;
    }

    public void addPerson(Person person) {
        this.persons.add(person);
    }

}