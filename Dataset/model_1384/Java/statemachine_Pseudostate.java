





import java.util.List;
import java.util.ArrayList;

public class statemachine_Pseudostate extends Vertex {

    private String id;
    private String kind;



    public statemachine_Pseudostate(
        String id,        String kind    ) {
        super(
        );
        this.id = id;
        this.kind = kind;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }


}