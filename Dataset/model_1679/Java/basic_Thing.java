





import java.util.List;
import java.util.ArrayList;

public class basic_Thing  {

    private int id;





    private basic_World basic_world;


    public basic_Thing(
        int id    ) {
        this.id = id;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public basic_World getBasic_world() {
        return basic_world;
    }

    public void setBasic_world(basic_World basic_world) {
        this.basic_world = basic_world;
    }

}