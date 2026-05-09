





import java.util.List;
import java.util.ArrayList;

public class simpleworld102_World extends Named {






    private List<simpleworld102_Thing> simpleworld102_things;




    private List<simpleworld102_Person> simpleworld102_persons;


    public simpleworld102_World(
    ) {
        super(
        );
        this.simpleworld102_things = new ArrayList<>();
        this.simpleworld102_persons = new ArrayList<>();
    }

    public simpleworld102_World(
        ArrayList<simpleworld102_Thing> simpleworld102_things,        ArrayList<simpleworld102_Person> simpleworld102_persons    ) {
        this.simpleworld102_things = simpleworld102_things;
        this.simpleworld102_persons = simpleworld102_persons;
    }


    public List<simpleworld102_Thing> getSimpleworld102_things() {
        return simpleworld102_things;
    }

    public void addSimpleworld102_thing(Simpleworld102_thing simpleworld102_thing) {
        this.simpleworld102_things.add(simpleworld102_thing);
    }
    public List<simpleworld102_Person> getSimpleworld102_persons() {
        return simpleworld102_persons;
    }

    public void addSimpleworld102_person(Simpleworld102_person simpleworld102_person) {
        this.simpleworld102_persons.add(simpleworld102_person);
    }

}