





import java.util.List;
import java.util.ArrayList;

public class stuff_World  {






    private List<stuff_Property> stuff_propertys;




    private List<stuff_Thing> stuff_things;


    public stuff_World(
    ) {
        this.stuff_propertys = new ArrayList<>();
        this.stuff_things = new ArrayList<>();
    }

    public stuff_World(
        ArrayList<stuff_Property> stuff_propertys,        ArrayList<stuff_Thing> stuff_things    ) {
        this.stuff_propertys = stuff_propertys;
        this.stuff_things = stuff_things;
    }


    public List<stuff_Property> getStuff_propertys() {
        return stuff_propertys;
    }

    public void addStuff_property(Stuff_property stuff_property) {
        this.stuff_propertys.add(stuff_property);
    }
    public List<stuff_Thing> getStuff_things() {
        return stuff_things;
    }

    public void addStuff_thing(Stuff_thing stuff_thing) {
        this.stuff_things.add(stuff_thing);
    }

}