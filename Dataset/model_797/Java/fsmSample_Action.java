





import java.util.List;
import java.util.ArrayList;

public class fsmSample_Action  {

    private String name;





    private fsmSample_Transition fsmsample_transition;


    public fsmSample_Action(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public fsmSample_Transition getFsmsample_transition() {
        return fsmsample_transition;
    }

    public void setFsmsample_transition(fsmSample_Transition fsmsample_transition) {
        this.fsmsample_transition = fsmsample_transition;
    }

}