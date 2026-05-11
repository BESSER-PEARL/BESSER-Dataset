





import java.util.List;
import java.util.ArrayList;

public class fair_YouthClub  {

    private String comments;
    private String name;





    private List<fair_Person> fair_persons;




    private fair_Fair fair_fair;


    public fair_YouthClub(
        String comments,        String name    ) {
        this.comments = comments;
        this.name = name;
        this.fair_persons = new ArrayList<>();
    }

    public fair_YouthClub(
        String comments,        String name        ArrayList<fair_Person> fair_persons    ) {
        this.comments = comments;
        this.name = name;
        this.fair_persons = fair_persons;
    }

    public String getComments() {
        return comments;
    }

    public void setComments(String comments) {
        this.comments = comments;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<fair_Person> getFair_persons() {
        return fair_persons;
    }

    public void addFair_person(Fair_person fair_person) {
        this.fair_persons.add(fair_person);
    }
    public fair_Fair getFair_fair() {
        return fair_fair;
    }

    public void setFair_fair(fair_Fair fair_fair) {
        this.fair_fair = fair_fair;
    }

}