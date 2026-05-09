





import java.util.List;
import java.util.ArrayList;

public class visualworld_Thing extends NamedElement {

    private int id;





    private visualworld_World visualworld_world;


    public visualworld_Thing(
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

    public visualworld_World getVisualworld_world() {
        return visualworld_world;
    }

    public void setVisualworld_world(visualworld_World visualworld_world) {
        this.visualworld_world = visualworld_world;
    }

}