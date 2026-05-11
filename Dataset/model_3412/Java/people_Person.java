





import java.util.List;
import java.util.ArrayList;

public class people_Person  {

    private String name;
    private String gender;





    private List<people_Person> people_persons;




    private people_Universe people_universe;




    private people_Person people_person;


    public people_Person(
        String name,        String gender    ) {
        this.name = name;
        this.gender = gender;
        this.people_persons = new ArrayList<>();
    }

    public people_Person(
        String name,        String gender        ArrayList<people_Person> people_persons    ) {
        this.name = name;
        this.gender = gender;
        this.people_persons = people_persons;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getGender() {
        return gender;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }

    public List<people_Person> getPeople_persons() {
        return people_persons;
    }

    public void addPeople_person(People_person people_person) {
        this.people_persons.add(people_person);
    }
    public people_Universe getPeople_universe() {
        return people_universe;
    }

    public void setPeople_universe(people_Universe people_universe) {
        this.people_universe = people_universe;
    }
    public people_Person getPeople_person() {
        return people_person;
    }

    public void setPeople_person(people_Person people_person) {
        this.people_person = people_person;
    }

}