





import java.util.List;
import java.util.ArrayList;

public class statemachine_Pseudostate extends Vertex {

    private String kind;
    private String id;



    public statemachine_Pseudostate(
        String kind,        String id    ) {
        super(
        );
        this.kind = kind;
        this.id = id;
    }


    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }


}