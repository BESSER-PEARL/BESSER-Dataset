





import java.util.List;
import java.util.ArrayList;

public class family_Person  {

    private String name;





    private List<family_Person> family_persons;




    private family_Person family_person;




    private family_Family family_family;




    private List<family_Person> family_persons;


    public family_Person(
        String name    ) {
        this.name = name;
        this.family_persons = new ArrayList<>();
        this.family_persons = new ArrayList<>();
    }

    public family_Person(
        String name        ArrayList<family_Person> family_persons,        ArrayList<family_Person> family_persons    ) {
        this.name = name;
        this.family_persons = family_persons;
        this.family_persons = family_persons;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<family_Person> getFamily_persons() {
        return family_persons;
    }

    public void addFamily_person(Family_person family_person) {
        this.family_persons.add(family_person);
    }
    public family_Person getFamily_person() {
        return family_person;
    }

    public void setFamily_person(family_Person family_person) {
        this.family_person = family_person;
    }
    public family_Family getFamily_family() {
        return family_family;
    }

    public void setFamily_family(family_Family family_family) {
        this.family_family = family_family;
    }
    public List<family_Person> getFamily_persons() {
        return family_persons;
    }

    public void addFamily_person(Family_person family_person) {
        this.family_persons.add(family_person);
    }

}