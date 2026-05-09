





import java.util.List;
import java.util.ArrayList;

public class nested103_Thing extends NamedElement {

    private int id;





    private nested103_World nested103_world;


    public nested103_Thing(
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

    public nested103_World getNested103_world() {
        return nested103_world;
    }

    public void setNested103_world(nested103_World nested103_world) {
        this.nested103_world = nested103_world;
    }

}