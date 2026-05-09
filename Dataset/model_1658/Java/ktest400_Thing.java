





import java.util.List;
import java.util.ArrayList;

public class ktest400_Thing extends NamedElement {

    private int id;





    private ktest400_World ktest400_world;


    public ktest400_Thing(
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

    public ktest400_World getKtest400_world() {
        return ktest400_world;
    }

    public void setKtest400_world(ktest400_World ktest400_world) {
        this.ktest400_world = ktest400_world;
    }

}