





import java.util.List;
import java.util.ArrayList;

public class statemachine_Pseudostate extends Node {

    private String pseudoType;



    public statemachine_Pseudostate(
        String pseudoType    ) {
        super(
        );
        this.pseudoType = pseudoType;
    }


    public String getPseudotype() {
        return pseudoType;
    }

    public void setPseudotype(String pseudoType) {
        this.pseudoType = pseudoType;
    }


}