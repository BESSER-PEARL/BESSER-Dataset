





import java.util.List;
import java.util.ArrayList;

public class rel2rel_World  {






    private List<rel2rel_Thing> rel2rel_things;


    public rel2rel_World(
    ) {
        this.rel2rel_things = new ArrayList<>();
    }

    public rel2rel_World(
        ArrayList<rel2rel_Thing> rel2rel_things    ) {
        this.rel2rel_things = rel2rel_things;
    }


    public List<rel2rel_Thing> getRel2rel_things() {
        return rel2rel_things;
    }

    public void addRel2rel_thing(Rel2rel_thing rel2rel_thing) {
        this.rel2rel_things.add(rel2rel_thing);
    }

}