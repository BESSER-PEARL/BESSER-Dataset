





import java.util.List;
import java.util.ArrayList;

public class simpleworld101_World extends Named {






    private List<simpleworld101_Person> simpleworld101_persons;




    private List<simpleworld101_Thing> simpleworld101_things;


    public simpleworld101_World(
    ) {
        super(
        );
        this.simpleworld101_persons = new ArrayList<>();
        this.simpleworld101_things = new ArrayList<>();
    }

    public simpleworld101_World(
        ArrayList<simpleworld101_Person> simpleworld101_persons,        ArrayList<simpleworld101_Thing> simpleworld101_things    ) {
        this.simpleworld101_persons = simpleworld101_persons;
        this.simpleworld101_things = simpleworld101_things;
    }


    public List<simpleworld101_Person> getSimpleworld101_persons() {
        return simpleworld101_persons;
    }

    public void addSimpleworld101_person(Simpleworld101_person simpleworld101_person) {
        this.simpleworld101_persons.add(simpleworld101_person);
    }
    public List<simpleworld101_Thing> getSimpleworld101_things() {
        return simpleworld101_things;
    }

    public void addSimpleworld101_thing(Simpleworld101_thing simpleworld101_thing) {
        this.simpleworld101_things.add(simpleworld101_thing);
    }

}