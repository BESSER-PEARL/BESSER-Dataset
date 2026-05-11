





import java.util.List;
import java.util.ArrayList;

public class behavioral_elements_state_machines_StubState extends StateVertex {

    private String referenceState;



    public behavioral_elements_state_machines_StubState(
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