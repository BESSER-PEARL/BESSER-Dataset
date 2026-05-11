





import java.util.List;
import java.util.ArrayList;

public class PersonList_WorkPlace  {

    private String address;





    private List<PersonList_Person> personlist_persons;




    private PersonList_Person personlist_person;




    private PersonList_List personlist_list;


    public PersonList_WorkPlace(
        String address    ) {
        this.address = address;
        this.personlist_persons = new ArrayList<>();
    }

    public PersonList_WorkPlace(
        String address        ArrayList<PersonList_Person> personlist_persons    ) {
        this.address = address;
        this.personlist_persons = personlist_persons;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public List<PersonList_Person> getPersonlist_persons() {
        return personlist_persons;
    }

    public void addPersonlist_person(Personlist_person personlist_person) {
        this.personlist_persons.add(personlist_person);
    }
    public PersonList_Person getPersonlist_person() {
        return personlist_person;
    }

    public void setPersonlist_person(PersonList_Person personlist_person) {
        this.personlist_person = personlist_person;
    }
    public PersonList_List getPersonlist_list() {
        return personlist_list;
    }

    public void setPersonlist_list(PersonList_List personlist_list) {
        this.personlist_list = personlist_list;
    }

}