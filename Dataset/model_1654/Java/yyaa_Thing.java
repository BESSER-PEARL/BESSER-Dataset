





import java.util.List;
import java.util.ArrayList;

public class yyaa_Thing extends NamedElement {

    private int id;





    private yyaa_World yyaa_world;


    public yyaa_Thing(
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

    public yyaa_World getYyaa_world() {
        return yyaa_world;
    }

    public void setYyaa_world(yyaa_World yyaa_world) {
        this.yyaa_world = yyaa_world;
    }

}