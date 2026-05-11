





import java.util.List;
import java.util.ArrayList;

public class Friends_Classroom  {

    private int id;





    private List<Friends_Person> friends_persons;




    private Friends_Person friends_person;


    public Friends_Classroom(
        int id    ) {
        this.id = id;
        this.friends_persons = new ArrayList<>();
    }

    public Friends_Classroom(
        int id        ArrayList<Friends_Person> friends_persons    ) {
        this.id = id;
        this.friends_persons = friends_persons;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public List<Friends_Person> getFriends_persons() {
        return friends_persons;
    }

    public void addFriends_person(Friends_person friends_person) {
        this.friends_persons.add(friends_person);
    }
    public Friends_Person getFriends_person() {
        return friends_person;
    }

    public void setFriends_person(Friends_Person friends_person) {
        this.friends_person = friends_person;
    }

}