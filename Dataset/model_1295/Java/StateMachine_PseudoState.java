





import java.util.List;
import java.util.ArrayList;

public class StateMachine_PseudoState extends Vertex {

    private String returnValue;
    private String pseudoStateKind;



    public StateMachine_PseudoState(
        String returnValue,        String pseudoStateKind    ) {
        super(
        );
        this.returnValue = returnValue;
        this.pseudoStateKind = pseudoStateKind;
    }


    public String getReturnvalue() {
        return returnValue;
    }

    public void setReturnvalue(String returnValue) {
        this.returnValue = returnValue;
    }
    public String getPseudostatekind() {
        return pseudoStateKind;
    }

    public void setPseudostatekind(String pseudoStateKind) {
        this.pseudoStateKind = pseudoStateKind;
    }


}