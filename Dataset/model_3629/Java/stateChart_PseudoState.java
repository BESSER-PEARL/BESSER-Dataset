





import java.util.List;
import java.util.ArrayList;

public class stateChart_PseudoState extends Vertex {

    private String PseudoStateType;



    public stateChart_PseudoState(
        String PseudoStateType    ) {
        super(
        );
        this.PseudoStateType = PseudoStateType;
    }


    public String getPseudostatetype() {
        return PseudoStateType;
    }

    public void setPseudostatetype(String PseudoStateType) {
        this.PseudoStateType = PseudoStateType;
    }


}