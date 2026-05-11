





import java.util.List;
import java.util.ArrayList;

public class basicfamily_Family  {

    private String name;





    private List<basicfamily_Person> basicfamily_persons;


    public basicfamily_Family(
        String name    ) {
        this.name = name;
        this.basicfamily_persons = new ArrayList<>();
    }

    public basicfamily_Family(
        String name        ArrayList<basicfamily_Person> basicfamily_persons    ) {
        this.name = name;
        this.basicfamily_persons = basicfamily_persons;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<basicfamily_Person> getBasicfamily_persons() {
        return basicfamily_persons;
    }

    public void addBasicfamily_person(Basicfamily_person basicfamily_person) {
        this.basicfamily_persons.add(basicfamily_person);
    }

}