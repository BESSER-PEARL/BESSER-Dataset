





import java.util.List;
import java.util.ArrayList;

public class fsm_VarRef extends Literal {

    private String varId;



    public fsm_VarRef(
        String varId    ) {
        super(
        );
        this.varId = varId;
    }


    public String getVarid() {
        return varId;
    }

    public void setVarid(String varId) {
        this.varId = varId;
    }


}