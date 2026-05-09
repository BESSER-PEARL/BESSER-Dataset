





import java.util.List;
import java.util.ArrayList;

public class family_ecore_Person  {

    private int age;
    private String name;





    private family_ecore_Person family_ecore_person;




    private family_ecore_Person family_ecore_person;




    private List<family_ecore_Person> family_ecore_persons;


    public family_ecore_Person(
        int age,        String name    ) {
        this.age = age;
        this.name = name;
        this.family_ecore_persons = new ArrayList<>();
    }

    public family_ecore_Person(
        int age,        String name        ArrayList<family_ecore_Person> family_ecore_persons    ) {
        this.age = age;
        this.name = name;
        this.family_ecore_persons = family_ecore_persons;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public family_ecore_Person getFamily_ecore_person() {
        return family_ecore_person;
    }

    public void setFamily_ecore_person(family_ecore_Person family_ecore_person) {
        this.family_ecore_person = family_ecore_person;
    }
    public family_ecore_Person getFamily_ecore_person() {
        return family_ecore_person;
    }

    public void setFamily_ecore_person(family_ecore_Person family_ecore_person) {
        this.family_ecore_person = family_ecore_person;
    }
    public List<family_ecore_Person> getFamily_ecore_persons() {
        return family_ecore_persons;
    }

    public void addFamily_ecore_person(Family_ecore_person family_ecore_person) {
        this.family_ecore_persons.add(family_ecore_person);
    }

}