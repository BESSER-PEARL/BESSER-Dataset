





import java.util.List;
import java.util.ArrayList;

public class fair_YoungPerson extends Person {






    private fair_YouthClub fair_youthclub;




    private List<fair_Person> fair_persons;


    public fair_YoungPerson(
    ) {
        super(
        );
        this.fair_persons = new ArrayList<>();
    }

    public fair_YoungPerson(
        ArrayList<fair_Person> fair_persons    ) {
        this.fair_persons = fair_persons;
    }


    public fair_YouthClub getFair_youthclub() {
        return fair_youthclub;
    }

    public void setFair_youthclub(fair_YouthClub fair_youthclub) {
        this.fair_youthclub = fair_youthclub;
    }
    public List<fair_Person> getFair_persons() {
        return fair_persons;
    }

    public void addFair_person(Fair_person fair_person) {
        this.fair_persons.add(fair_person);
    }

}