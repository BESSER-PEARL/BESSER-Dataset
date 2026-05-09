





import java.util.List;
import java.util.ArrayList;

public class family_ecore_Family  {






    private List<family_ecore_Person> family_ecore_persons;


    public family_ecore_Family(
    ) {
        this.family_ecore_persons = new ArrayList<>();
    }

    public family_ecore_Family(
        ArrayList<family_ecore_Person> family_ecore_persons    ) {
        this.family_ecore_persons = family_ecore_persons;
    }


    public List<family_ecore_Person> getFamily_ecore_persons() {
        return family_ecore_persons;
    }

    public void addFamily_ecore_person(Family_ecore_person family_ecore_person) {
        this.family_ecore_persons.add(family_ecore_person);
    }

}