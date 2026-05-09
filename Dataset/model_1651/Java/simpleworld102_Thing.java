





import java.util.List;
import java.util.ArrayList;

public class simpleworld102_Thing extends Named {






    private List<simpleworld102_Person> simpleworld102_persons;




    private simpleworld102_Person simpleworld102_person;




    private simpleworld102_Thing simpleworld102_thing;




    private simpleworld102_Person simpleworld102_person;


    public simpleworld102_Thing(
    ) {
        super(
        );
        this.simpleworld102_persons = new ArrayList<>();
    }

    public simpleworld102_Thing(
        ArrayList<simpleworld102_Person> simpleworld102_persons    ) {
        this.simpleworld102_persons = simpleworld102_persons;
    }


    public List<simpleworld102_Person> getSimpleworld102_persons() {
        return simpleworld102_persons;
    }

    public void addSimpleworld102_person(Simpleworld102_person simpleworld102_person) {
        this.simpleworld102_persons.add(simpleworld102_person);
    }
    public simpleworld102_Person getSimpleworld102_person() {
        return simpleworld102_person;
    }

    public void setSimpleworld102_person(simpleworld102_Person simpleworld102_person) {
        this.simpleworld102_person = simpleworld102_person;
    }
    public simpleworld102_Thing getSimpleworld102_thing() {
        return simpleworld102_thing;
    }

    public void setSimpleworld102_thing(simpleworld102_Thing simpleworld102_thing) {
        this.simpleworld102_thing = simpleworld102_thing;
    }
    public simpleworld102_Person getSimpleworld102_person() {
        return simpleworld102_person;
    }

    public void setSimpleworld102_person(simpleworld102_Person simpleworld102_person) {
        this.simpleworld102_person = simpleworld102_person;
    }

}