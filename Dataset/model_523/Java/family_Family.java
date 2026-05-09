





import java.util.List;
import java.util.ArrayList;

public class family_Family extends FNamedElement {






    private List<family_Person> family_persons;


    public family_Family(
    ) {
        super(
        );
        this.family_persons = new ArrayList<>();
    }

    public family_Family(
        ArrayList<family_Person> family_persons    ) {
        this.family_persons = family_persons;
    }


    public List<family_Person> getFamily_persons() {
        return family_persons;
    }

    public void addFamily_person(Family_person family_person) {
        this.family_persons.add(family_person);
    }

}