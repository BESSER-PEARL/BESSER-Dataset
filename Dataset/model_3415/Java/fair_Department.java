





import java.util.List;
import java.util.ArrayList;

public class fair_Department  {

    private String name;
    private String comments;





    private fair_Division fair_division;




    private fair_Division fair_division;




    private List<fair_Person> fair_persons;


    public fair_Department(
        String name,        String comments    ) {
        this.name = name;
        this.comments = comments;
        this.fair_persons = new ArrayList<>();
    }

    public fair_Department(
        String name,        String comments        ArrayList<fair_Person> fair_persons    ) {
        this.name = name;
        this.comments = comments;
        this.fair_persons = fair_persons;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getComments() {
        return comments;
    }

    public void setComments(String comments) {
        this.comments = comments;
    }

    public fair_Division getFair_division() {
        return fair_division;
    }

    public void setFair_division(fair_Division fair_division) {
        this.fair_division = fair_division;
    }
    public fair_Division getFair_division() {
        return fair_division;
    }

    public void setFair_division(fair_Division fair_division) {
        this.fair_division = fair_division;
    }
    public List<fair_Person> getFair_persons() {
        return fair_persons;
    }

    public void addFair_person(Fair_person fair_person) {
        this.fair_persons.add(fair_person);
    }

}