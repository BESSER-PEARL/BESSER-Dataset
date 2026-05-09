





import java.util.List;
import java.util.ArrayList;

public class fsm_RuntimeConcept1  {

    private int foo;





    private fsm_State fsm_state;


    public fsm_RuntimeConcept1(
        int foo    ) {
        this.foo = foo;
    }


    public int getFoo() {
        return foo;
    }

    public void setFoo(int foo) {
        this.foo = foo;
    }

    public fsm_State getFsm_state() {
        return fsm_state;
    }

    public void setFsm_state(fsm_State fsm_state) {
        this.fsm_state = fsm_state;
    }

}