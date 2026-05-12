





import java.util.List;
import java.util.ArrayList;

public class sgraph_Entry extends Pseudostate {

    private String kind;



    public sgraph_Entry(
        String kind    ) {
        super(
        );
        this.kind = kind;
    }


    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }


}