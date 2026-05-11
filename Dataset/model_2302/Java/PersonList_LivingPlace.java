





import java.util.List;
import java.util.ArrayList;

public class PersonList_LivingPlace extends Place {






    private PersonList_Person personlist_person;




    private List<PersonList_Person> personlist_persons;


    public PersonList_LivingPlace(
    ) {
        super(
        );
        this.personlist_persons = new ArrayList<>();
    }

    public PersonList_LivingPlace(
        ArrayList<PersonList_Person> personlist_persons    ) {
        this.personlist_persons = personlist_persons;
    }


    public PersonList_Person getPersonlist_person() {
        return personlist_person;
    }

    public void setPersonlist_person(PersonList_Person personlist_person) {
        this.personlist_person = personlist_person;
    }
    public List<PersonList_Person> getPersonlist_persons() {
        return personlist_persons;
    }

    public void addPersonlist_person(Personlist_person personlist_person) {
        this.personlist_persons.add(personlist_person);
    }

}