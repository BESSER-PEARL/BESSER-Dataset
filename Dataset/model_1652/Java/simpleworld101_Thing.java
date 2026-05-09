





import java.util.List;
import java.util.ArrayList;

public class simpleworld101_Thing extends Named {






    private simpleworld101_Person simpleworld101_person;




    private simpleworld101_Thing simpleworld101_thing;




    private List<simpleworld101_Person> simpleworld101_persons;




    private simpleworld101_Person simpleworld101_person;


    public simpleworld101_Thing(
    ) {
        super(
        );
        this.simpleworld101_persons = new ArrayList<>();
    }

    public simpleworld101_Thing(
        ArrayList<simpleworld101_Person> simpleworld101_persons    ) {
        this.simpleworld101_persons = simpleworld101_persons;
    }


    public simpleworld101_Person getSimpleworld101_person() {
        return simpleworld101_person;
    }

    public void setSimpleworld101_person(simpleworld101_Person simpleworld101_person) {
        this.simpleworld101_person = simpleworld101_person;
    }
    public simpleworld101_Thing getSimpleworld101_thing() {
        return simpleworld101_thing;
    }

    public void setSimpleworld101_thing(simpleworld101_Thing simpleworld101_thing) {
        this.simpleworld101_thing = simpleworld101_thing;
    }
    public List<simpleworld101_Person> getSimpleworld101_persons() {
        return simpleworld101_persons;
    }

    public void addSimpleworld101_person(Simpleworld101_person simpleworld101_person) {
        this.simpleworld101_persons.add(simpleworld101_person);
    }
    public simpleworld101_Person getSimpleworld101_person() {
        return simpleworld101_person;
    }

    public void setSimpleworld101_person(simpleworld101_Person simpleworld101_person) {
        this.simpleworld101_person = simpleworld101_person;
    }

}