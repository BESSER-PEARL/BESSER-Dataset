





import java.util.List;
import java.util.ArrayList;

public class family_ecore_Person  {

    private String name;
    private float height;
    private int age;





    private family_ecore_Person family_ecore_person;




    private List<family_ecore_Person> family_ecore_persons;




    private List<family_ecore_Person> family_ecore_persons;


    public family_ecore_Person(
        String name,        float height,        int age    ) {
        this.name = name;
        this.height = height;
        this.age = age;
        this.family_ecore_persons = new ArrayList<>();
        this.family_ecore_persons = new ArrayList<>();
    }

    public family_ecore_Person(
        String name,        float height,        int age        ArrayList<family_ecore_Person> family_ecore_persons,        ArrayList<family_ecore_Person> family_ecore_persons    ) {
        this.name = name;
        this.height = height;
        this.age = age;
        this.family_ecore_persons = family_ecore_persons;
        this.family_ecore_persons = family_ecore_persons;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public float getHeight() {
        return height;
    }

    public void setHeight(float height) {
        this.height = height;
    }
    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
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
    public List<family_ecore_Person> getFamily_ecore_persons() {
        return family_ecore_persons;
    }

    public void addFamily_ecore_person(Family_ecore_person family_ecore_person) {
        this.family_ecore_persons.add(family_ecore_person);
    }

}