





import java.util.List;
import java.util.ArrayList;

public class simpleworld_World  {






    private List<simpleworld_Thing> simpleworld_things;


    public simpleworld_World(
    ) {
        this.simpleworld_things = new ArrayList<>();
    }

    public simpleworld_World(
        ArrayList<simpleworld_Thing> simpleworld_things    ) {
        this.simpleworld_things = simpleworld_things;
    }


    public List<simpleworld_Thing> getSimpleworld_things() {
        return simpleworld_things;
    }

    public void addSimpleworld_thing(Simpleworld_thing simpleworld_thing) {
        this.simpleworld_things.add(simpleworld_thing);
    }

}