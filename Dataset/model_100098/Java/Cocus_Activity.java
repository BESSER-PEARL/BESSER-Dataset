





import java.util.List;
import java.util.ArrayList;

public class Cocus_Activity  {






    private List<Thing> things;




    private Person person;


    public Cocus_Activity(
    ) {
        this.things = new ArrayList<>();
    }

    public Cocus_Activity(
        ArrayList<Thing> things    ) {
        this.things = things;
    }


    public List<Thing> getThings() {
        return things;
    }

    public void addThing(Thing thing) {
        this.things.add(thing);
    }
    public Person getPerson() {
        return person;
    }

    public void setPerson(Person person) {
        this.person = person;
    }

}