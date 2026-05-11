





import java.util.List;
import java.util.ArrayList;

public class Persons_Facility extends NamedElement {






    private List<Persons_Person> persons_persons;




    private Persons_District persons_district;


    public Persons_Facility(
    ) {
        super(
        );
        this.persons_persons = new ArrayList<>();
    }

    public Persons_Facility(
        ArrayList<Persons_Person> persons_persons    ) {
        this.persons_persons = persons_persons;
    }


    public List<Persons_Person> getPersons_persons() {
        return persons_persons;
    }

    public void addPersons_person(Persons_person persons_person) {
        this.persons_persons.add(persons_person);
    }
    public Persons_District getPersons_district() {
        return persons_district;
    }

    public void setPersons_district(Persons_District persons_district) {
        this.persons_district = persons_district;
    }

}