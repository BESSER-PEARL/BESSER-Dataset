





import java.util.List;
import java.util.ArrayList;

public class nested102_Thing extends NamedElement {

    private int id;





    private nested102_World nested102_world;


    public nested102_Thing(
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

    public nested102_World getNested102_world() {
        return nested102_world;
    }

    public void setNested102_world(nested102_World nested102_world) {
        this.nested102_world = nested102_world;
    }

}