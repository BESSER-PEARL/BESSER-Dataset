





import java.util.List;
import java.util.ArrayList;

public class Friends_Person  {

    private String name;





    private List<Friends_Person> friends_persons;


    public Friends_Person(
        String name    ) {
        this.name = name;
        this.friends_persons = new ArrayList<>();
    }

    public Friends_Person(
        String name        ArrayList<Friends_Person> friends_persons    ) {
        this.name = name;
        this.friends_persons = friends_persons;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<Friends_Person> getFriends_persons() {
        return friends_persons;
    }

    public void addFriends_person(Friends_person friends_person) {
        this.friends_persons.add(friends_person);
    }

}