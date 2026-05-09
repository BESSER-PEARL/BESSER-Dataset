





import java.util.List;
import java.util.ArrayList;

public class families_Person extends NamedElement {






    private List<families_Person> families_persons;




    private families_Family families_family;




    private families_Person families_person;




    private families_Person families_person;


    public families_Person(
    ) {
        super(
        );
        this.families_persons = new ArrayList<>();
    }

    public families_Person(
        ArrayList<families_Person> families_persons    ) {
        this.families_persons = families_persons;
    }


    public List<families_Person> getFamilies_persons() {
        return families_persons;
    }

    public void addFamilies_person(Families_person families_person) {
        this.families_persons.add(families_person);
    }
    public families_Family getFamilies_family() {
        return families_family;
    }

    public void setFamilies_family(families_Family families_family) {
        this.families_family = families_family;
    }
    public families_Person getFamilies_person() {
        return families_person;
    }

    public void setFamilies_person(families_Person families_person) {
        this.families_person = families_person;
    }
    public families_Person getFamilies_person() {
        return families_person;
    }

    public void setFamilies_person(families_Person families_person) {
        this.families_person = families_person;
    }

}