





import java.util.List;
import java.util.ArrayList;

public class stuff_Thing  {

    private int id;





    private stuff_World stuff_world;




    private List<stuff_Thing> stuff_things;




    private stuff_Foo stuff_foo;


    public stuff_Thing(
        int id    ) {
        this.id = id;
        this.stuff_things = new ArrayList<>();
    }

    public stuff_Thing(
        int id        ArrayList<stuff_Thing> stuff_things    ) {
        this.id = id;
        this.stuff_things = stuff_things;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public stuff_World getStuff_world() {
        return stuff_world;
    }

    public void setStuff_world(stuff_World stuff_world) {
        this.stuff_world = stuff_world;
    }
    public List<stuff_Thing> getStuff_things() {
        return stuff_things;
    }

    public void addStuff_thing(Stuff_thing stuff_thing) {
        this.stuff_things.add(stuff_thing);
    }
    public stuff_Foo getStuff_foo() {
        return stuff_foo;
    }

    public void setStuff_foo(stuff_Foo stuff_foo) {
        this.stuff_foo = stuff_foo;
    }

}