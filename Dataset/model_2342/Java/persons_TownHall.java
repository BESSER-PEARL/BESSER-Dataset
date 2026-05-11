





import java.util.List;
import java.util.ArrayList;

public class persons_TownHall extends NamedElement {






    private List<persons_Person> persons_persons;




    private List<persons_District> persons_districts;




    private persons_Community persons_community;




    private persons_Committee persons_committee;


    public persons_TownHall(
    ) {
        super(
        );
        this.persons_persons = new ArrayList<>();
        this.persons_districts = new ArrayList<>();
    }

    public persons_TownHall(
        ArrayList<persons_Person> persons_persons,        ArrayList<persons_District> persons_districts    ) {
        this.persons_persons = persons_persons;
        this.persons_districts = persons_districts;
    }


    public List<persons_Person> getPersons_persons() {
        return persons_persons;
    }

    public void addPersons_person(Persons_person persons_person) {
        this.persons_persons.add(persons_person);
    }
    public List<persons_District> getPersons_districts() {
        return persons_districts;
    }

    public void addPersons_district(Persons_district persons_district) {
        this.persons_districts.add(persons_district);
    }
    public persons_Community getPersons_community() {
        return persons_community;
    }

    public void setPersons_community(persons_Community persons_community) {
        this.persons_community = persons_community;
    }
    public persons_Committee getPersons_committee() {
        return persons_committee;
    }

    public void setPersons_committee(persons_Committee persons_committee) {
        this.persons_committee = persons_committee;
    }

}