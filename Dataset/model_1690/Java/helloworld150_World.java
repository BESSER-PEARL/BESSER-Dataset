





import java.util.List;
import java.util.ArrayList;

public class helloworld150_World  {






    private List<helloworld150_Person> helloworld150_persons;




    private List<helloworld150_Thing> helloworld150_things;


    public helloworld150_World(
    ) {
        this.helloworld150_persons = new ArrayList<>();
        this.helloworld150_things = new ArrayList<>();
    }

    public helloworld150_World(
        ArrayList<helloworld150_Person> helloworld150_persons,        ArrayList<helloworld150_Thing> helloworld150_things    ) {
        this.helloworld150_persons = helloworld150_persons;
        this.helloworld150_things = helloworld150_things;
    }


    public List<helloworld150_Person> getHelloworld150_persons() {
        return helloworld150_persons;
    }

    public void addHelloworld150_person(Helloworld150_person helloworld150_person) {
        this.helloworld150_persons.add(helloworld150_person);
    }
    public List<helloworld150_Thing> getHelloworld150_things() {
        return helloworld150_things;
    }

    public void addHelloworld150_thing(Helloworld150_thing helloworld150_thing) {
        this.helloworld150_things.add(helloworld150_thing);
    }

}