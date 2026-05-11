





import java.util.List;
import java.util.ArrayList;

public class basicfamily_Person  {

    private String name;





    private List<basicfamily_Person> basicfamily_persons;




    private basicfamily_Person basicfamily_person;




    private basicfamily_Family basicfamily_family;


    public basicfamily_Person(
        String name    ) {
        this.name = name;
        this.basicfamily_persons = new ArrayList<>();
    }

    public basicfamily_Person(
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
    public basicfamily_Person getBasicfamily_person() {
        return basicfamily_person;
    }

    public void setBasicfamily_person(basicfamily_Person basicfamily_person) {
        this.basicfamily_person = basicfamily_person;
    }
    public basicfamily_Family getBasicfamily_family() {
        return basicfamily_family;
    }

    public void setBasicfamily_family(basicfamily_Family basicfamily_family) {
        this.basicfamily_family = basicfamily_family;
    }

}