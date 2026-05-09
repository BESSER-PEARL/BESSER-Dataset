





import java.util.List;
import java.util.ArrayList;

public class basic2_Thing  {

    private int id;





    private List<basic2_Thing> basic2_things;


    public basic2_Thing(
        int id    ) {
        this.id = id;
        this.basic2_things = new ArrayList<>();
    }

    public basic2_Thing(
        int id        ArrayList<basic2_Thing> basic2_things    ) {
        this.id = id;
        this.basic2_things = basic2_things;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public List<basic2_Thing> getBasic2_things() {
        return basic2_things;
    }

    public void addBasic2_thing(Basic2_thing basic2_thing) {
        this.basic2_things.add(basic2_thing);
    }

}