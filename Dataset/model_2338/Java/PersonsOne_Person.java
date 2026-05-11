





import java.util.List;
import java.util.ArrayList;

public class PersonsOne_Person  {

    private String name;
    private int age;





    private PersonsOne_Group personsone_group;


    public PersonsOne_Person(
        String name,        int age    ) {
        this.name = name;
        this.age = age;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public PersonsOne_Group getPersonsone_group() {
        return personsone_group;
    }

    public void setPersonsone_group(PersonsOne_Group personsone_group) {
        this.personsone_group = personsone_group;
    }

}