





import java.util.List;
import java.util.ArrayList;

public class fsm_Transition extends NamedElement {






    private fsm_Region fsm_region;


    public fsm_Transition(
    ) {
        super(
        );
    }



    public fsm_Region getFsm_region() {
        return fsm_region;
    }

    public void setFsm_region(fsm_Region fsm_region) {
        this.fsm_region = fsm_region;
    }

}