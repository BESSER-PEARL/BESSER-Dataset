





import java.util.List;
import java.util.ArrayList;

public class fsm_NoAnnotation extends NoAnnotationSuper {

    private String b;
    private String a;





    private fsm_FSM fsm_fsm;




    private List<fsm_State> fsm_states;


    public fsm_NoAnnotation(
        String b,        String a    ) {
        super(
        );
        this.b = b;
        this.a = a;
        this.fsm_states = new ArrayList<>();
    }

    public fsm_NoAnnotation(
        String b,        String a        ArrayList<fsm_State> fsm_states    ) {
        this.b = b;
        this.a = a;
        this.fsm_states = fsm_states;
    }

    public String getB() {
        return b;
    }

    public void setB(String b) {
        this.b = b;
    }
    public String getA() {
        return a;
    }

    public void setA(String a) {
        this.a = a;
    }

    public fsm_FSM getFsm_fsm() {
        return fsm_fsm;
    }

    public void setFsm_fsm(fsm_FSM fsm_fsm) {
        this.fsm_fsm = fsm_fsm;
    }
    public List<fsm_State> getFsm_states() {
        return fsm_states;
    }

    public void addFsm_state(Fsm_state fsm_state) {
        this.fsm_states.add(fsm_state);
    }

}