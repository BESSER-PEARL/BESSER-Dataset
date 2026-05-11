





import java.util.List;
import java.util.ArrayList;

public class Persons_TownHall extends NamedElement {






    private List<Persons_Person> persons_persons;




    private Persons_Community persons_community;


    public Persons_TownHall(
    ) {
        super(
        );
        this.persons_persons = new ArrayList<>();
    }

    public Persons_TownHall(
        ArrayList<Persons_Person> persons_persons    ) {
        this.persons_persons = persons_persons;
    }


    public List<Persons_Person> getPersons_persons() {
        return persons_persons;
    }

    public void addPersons_person(Persons_person persons_person) {
        this.persons_persons.add(persons_person);
    }
    public Persons_Community getPersons_community() {
        return persons_community;
    }

    public void setPersons_community(Persons_Community persons_community) {
        this.persons_community = persons_community;
    }

}