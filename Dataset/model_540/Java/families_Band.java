





import java.util.List;
import java.util.ArrayList;

public class families_Band  {






    private List<families_Person> families_persons;


    public families_Band(
    ) {
        this.families_persons = new ArrayList<>();
    }

    public families_Band(
        ArrayList<families_Person> families_persons    ) {
        this.families_persons = families_persons;
    }


    public List<families_Person> getFamilies_persons() {
        return families_persons;
    }

    public void addFamilies_person(Families_person families_person) {
        this.families_persons.add(families_person);
    }

}