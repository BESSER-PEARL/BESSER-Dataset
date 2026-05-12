





import java.util.List;
import java.util.ArrayList;

public class UHSM_State extends TracedClass {

    private String name;





    private UHSM_CompositeState uhsm_compositestate;




    private UHSM_UState uhsm_ustate;




    private UHSM_CompositeState uhsm_compositestate;




    private UHSM_StateMachine uhsm_statemachine;


    public UHSM_State(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public UHSM_CompositeState getUhsm_compositestate() {
        return uhsm_compositestate;
    }

    public void setUhsm_compositestate(UHSM_CompositeState uhsm_compositestate) {
        this.uhsm_compositestate = uhsm_compositestate;
    }
    public UHSM_UState getUhsm_ustate() {
        return uhsm_ustate;
    }

    public void setUhsm_ustate(UHSM_UState uhsm_ustate) {
        this.uhsm_ustate = uhsm_ustate;
    }
    public UHSM_CompositeState getUhsm_compositestate() {
        return uhsm_compositestate;
    }

    public void setUhsm_compositestate(UHSM_CompositeState uhsm_compositestate) {
        this.uhsm_compositestate = uhsm_compositestate;
    }
    public UHSM_StateMachine getUhsm_statemachine() {
        return uhsm_statemachine;
    }

    public void setUhsm_statemachine(UHSM_StateMachine uhsm_statemachine) {
        this.uhsm_statemachine = uhsm_statemachine;
    }

}