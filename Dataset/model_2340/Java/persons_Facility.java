





import java.util.List;
import java.util.ArrayList;

public class persons_Facility extends NamedElement {






    private List<persons_Person> persons_persons;


    public persons_Facility(
    ) {
        super(
        );
        this.persons_persons = new ArrayList<>();
    }

    public persons_Facility(
        ArrayList<persons_Person> persons_persons    ) {
        this.persons_persons = persons_persons;
    }


    public List<persons_Person> getPersons_persons() {
        return persons_persons;
    }

    public void addPersons_person(Persons_person persons_person) {
        this.persons_persons.add(persons_person);
    }

}