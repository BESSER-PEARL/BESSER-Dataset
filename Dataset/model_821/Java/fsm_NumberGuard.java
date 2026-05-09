





import java.util.List;
import java.util.ArrayList;

public class fsm_NumberGuard extends Guard {

    private boolean value;





    private fsm_NumberVariable fsm_numbervariable;


    public fsm_NumberGuard(
        boolean value    ) {
        super(
        );
        this.value = value;
    }


    public boolean getValue() {
        return value;
    }

    public void setValue(boolean value) {
        this.value = value;
    }

    public fsm_NumberVariable getFsm_numbervariable() {
        return fsm_numbervariable;
    }

    public void setFsm_numbervariable(fsm_NumberVariable fsm_numbervariable) {
        this.fsm_numbervariable = fsm_numbervariable;
    }

}