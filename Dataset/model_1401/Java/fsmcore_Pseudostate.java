





import java.util.List;
import java.util.ArrayList;

public class fsmcore_Pseudostate extends AbstractState {

    private String kind;



    public fsmcore_Pseudostate(
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