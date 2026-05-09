





import java.util.List;
import java.util.ArrayList;

public class helloworldsaved_Thing extends NamedElement {

    private int id;





    private helloworldsaved_World helloworldsaved_world;


    public helloworldsaved_Thing(
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

    public helloworldsaved_World getHelloworldsaved_world() {
        return helloworldsaved_world;
    }

    public void setHelloworldsaved_world(helloworldsaved_World helloworldsaved_world) {
        this.helloworldsaved_world = helloworldsaved_world;
    }

}