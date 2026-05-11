





import java.util.List;
import java.util.ArrayList;

public class fair_Fair  {

    private String comments;
    private String name;





    private fair_Premises fair_premises;




    private List<fair_Division> fair_divisions;




    private List<fair_Person> fair_persons;


    public fair_Fair(
        String comments,        String name    ) {
        this.comments = comments;
        this.name = name;
        this.fair_divisions = new ArrayList<>();
        this.fair_persons = new ArrayList<>();
    }

    public fair_Fair(
        String comments,        String name        ArrayList<fair_Division> fair_divisions,        ArrayList<fair_Person> fair_persons    ) {
        this.comments = comments;
        this.name = name;
        this.fair_divisions = fair_divisions;
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

    public fair_Premises getFair_premises() {
        return fair_premises;
    }

    public void setFair_premises(fair_Premises fair_premises) {
        this.fair_premises = fair_premises;
    }
    public List<fair_Division> getFair_divisions() {
        return fair_divisions;
    }

    public void addFair_division(Fair_division fair_division) {
        this.fair_divisions.add(fair_division);
    }
    public List<fair_Person> getFair_persons() {
        return fair_persons;
    }

    public void addFair_person(Fair_person fair_person) {
        this.fair_persons.add(fair_person);
    }

}