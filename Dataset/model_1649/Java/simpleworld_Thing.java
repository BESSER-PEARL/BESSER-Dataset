





import java.util.List;
import java.util.ArrayList;

public class simpleworld_Thing extends NamedElement {

    private int id;





    private simpleworld_World simpleworld_world;


    public simpleworld_Thing(
        int id    ) {
        super(
        );
        this.id = id;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public simpleworld_World getSimpleworld_world() {
        return simpleworld_world;
    }

    public void setSimpleworld_world(simpleworld_World simpleworld_world) {
        this.simpleworld_world = simpleworld_world;
    }

}