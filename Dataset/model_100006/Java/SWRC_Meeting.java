





import java.util.List;
import java.util.ArrayList;

public class SWRC_Meeting extends Event {

    private String title;





    private List<Person> persons;


    public SWRC_Meeting(
        String title    ) {
        super(
        );
        this.title = title;
        this.persons = new ArrayList<>();
    }

    public SWRC_Meeting(
        String title        ArrayList<Person> persons    ) {
        this.title = title;
        this.persons = persons;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public List<Person> getPersons() {
        return persons;
    }

    public void addPerson(Person person) {
        this.persons.add(person);
    }

}