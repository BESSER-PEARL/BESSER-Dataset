





import java.util.List;
import java.util.ArrayList;

public class basic2_World  {






    private List<basic2_Thing> basic2_things;


    public basic2_World(
    ) {
        this.basic2_things = new ArrayList<>();
    }

    public basic2_World(
        ArrayList<basic2_Thing> basic2_things    ) {
        this.basic2_things = basic2_things;
    }


    public List<basic2_Thing> getBasic2_things() {
        return basic2_things;
    }

    public void addBasic2_thing(Basic2_thing basic2_thing) {
        this.basic2_things.add(basic2_thing);
    }

}