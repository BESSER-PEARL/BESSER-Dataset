





import java.util.List;
import java.util.ArrayList;

public class persons_TownHall extends NamedElement {






    private List<persons_Person> persons_persons;




    private persons_Community persons_community;


    public persons_TownHall(
    ) {
        super(
        );
        this.persons_persons = new ArrayList<>();
    }

    public persons_TownHall(
        ArrayList<persons_Person> persons_persons    ) {
        this.persons_persons = persons_persons;
    }


    public List<persons_Person> getPersons_persons() {
        return persons_persons;
    }

    public void addPersons_person(Persons_person persons_person) {
        this.persons_persons.add(persons_person);
    }
    public persons_Community getPersons_community() {
        return persons_community;
    }

    public void setPersons_community(persons_Community persons_community) {
        this.persons_community = persons_community;
    }

}