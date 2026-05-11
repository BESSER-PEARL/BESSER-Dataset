





import java.util.List;
import java.util.ArrayList;

public class genealogy_Person  {

    private int age;
    private boolean alive;
    private String name;





    private genealogy_Genealogy genealogy_genealogy;




    private List<genealogy_Person> genealogy_persons;




    private List<genealogy_Person> genealogy_persons;


    public genealogy_Person(
        int age,        boolean alive,        String name    ) {
        this.age = age;
        this.alive = alive;
        this.name = name;
        this.genealogy_persons = new ArrayList<>();
        this.genealogy_persons = new ArrayList<>();
    }

    public genealogy_Person(
        int age,        boolean alive,        String name        ArrayList<genealogy_Person> genealogy_persons,        ArrayList<genealogy_Person> genealogy_persons    ) {
        this.age = age;
        this.alive = alive;
        this.name = name;
        this.genealogy_persons = genealogy_persons;
        this.genealogy_persons = genealogy_persons;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }
    public boolean getAlive() {
        return alive;
    }

    public void setAlive(boolean alive) {
        this.alive = alive;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public genealogy_Genealogy getGenealogy_genealogy() {
        return genealogy_genealogy;
    }

    public void setGenealogy_genealogy(genealogy_Genealogy genealogy_genealogy) {
        this.genealogy_genealogy = genealogy_genealogy;
    }
    public List<genealogy_Person> getGenealogy_persons() {
        return genealogy_persons;
    }

    public void addGenealogy_person(Genealogy_person genealogy_person) {
        this.genealogy_persons.add(genealogy_person);
    }
    public List<genealogy_Person> getGenealogy_persons() {
        return genealogy_persons;
    }

    public void addGenealogy_person(Genealogy_person genealogy_person) {
        this.genealogy_persons.add(genealogy_person);
    }

}