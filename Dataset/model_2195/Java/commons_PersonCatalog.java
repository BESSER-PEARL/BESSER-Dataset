





import java.util.List;
import java.util.ArrayList;

public class commons_PersonCatalog  {






    private List<commons_Person> commons_persons;


    public commons_PersonCatalog(
    ) {
        this.commons_persons = new ArrayList<>();
    }

    public commons_PersonCatalog(
        ArrayList<commons_Person> commons_persons    ) {
        this.commons_persons = commons_persons;
    }


    public List<commons_Person> getCommons_persons() {
        return commons_persons;
    }

    public void addCommons_person(Commons_person commons_person) {
        this.commons_persons.add(commons_person);
    }

}