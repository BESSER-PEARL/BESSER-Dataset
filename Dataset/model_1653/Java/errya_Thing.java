





import java.util.List;
import java.util.ArrayList;

public class errya_Thing extends NamedElement {

    private int id;





    private errya_World errya_world;


    public errya_Thing(
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

    public errya_World getErrya_world() {
        return errya_world;
    }

    public void setErrya_world(errya_World errya_world) {
        this.errya_world = errya_world;
    }

}