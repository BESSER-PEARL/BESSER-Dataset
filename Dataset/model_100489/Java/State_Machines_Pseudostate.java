





import java.util.List;
import java.util.ArrayList;

public class State_Machines_Pseudostate extends StateVertex {

    private String kind;



    public State_Machines_Pseudostate(
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