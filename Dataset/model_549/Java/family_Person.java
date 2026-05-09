





import java.util.List;
import java.util.ArrayList;

public class family_Person  {

    private int size;
    private int age;
    private String name;
    private int weight;





    private List<family_Person> family_persons;




    private family_Person family_person;


    public family_Person(
        int size,        int age,        String name,        int weight    ) {
        this.size = size;
        this.age = age;
        this.name = name;
        this.weight = weight;
        this.family_persons = new ArrayList<>();
    }

    public family_Person(
        int size,        int age,        String name,        int weight        ArrayList<family_Person> family_persons    ) {
        this.size = size;
        this.age = age;
        this.name = name;
        this.weight = weight;
        this.family_persons = family_persons;
    }

    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
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
    public int getWeight() {
        return weight;
    }

    public void setWeight(int weight) {
        this.weight = weight;
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

}