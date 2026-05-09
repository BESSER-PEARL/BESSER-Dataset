





import java.util.List;
import java.util.ArrayList;

public class state_PseudoState extends Vertex {

    private String kind;



    public state_PseudoState(
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