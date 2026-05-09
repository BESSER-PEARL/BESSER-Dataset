





import java.util.List;
import java.util.ArrayList;

public class fsm_Pseudostate extends AbstractState {

    private String kind;



    public fsm_Pseudostate(
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