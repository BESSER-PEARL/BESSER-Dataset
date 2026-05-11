





import java.util.List;
import java.util.ArrayList;

public class people_Universe  {






    private List<people_Person> people_persons;


    public people_Universe(
    ) {
        this.people_persons = new ArrayList<>();
    }

    public people_Universe(
        ArrayList<people_Person> people_persons    ) {
        this.people_persons = people_persons;
    }


    public List<people_Person> getPeople_persons() {
        return people_persons;
    }

    public void addPeople_person(People_person people_person) {
        this.people_persons.add(people_person);
    }

}