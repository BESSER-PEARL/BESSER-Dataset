





import java.util.List;
import java.util.ArrayList;

public class State_Machines_StubState extends StateVertex {

    private String referenceState;



    public State_Machines_StubState(
        String referenceState    ) {
        super(
        );
        this.referenceState = referenceState;
    }


    public String getReferencestate() {
        return referenceState;
    }

    public void setReferencestate(String referenceState) {
        this.referenceState = referenceState;
    }


}