





import java.util.List;
import java.util.ArrayList;

public class fsm_NumberGuard extends Guard {

    private int value;





    private fsm_NumberVariable fsm_numbervariable;


    public fsm_NumberGuard(
        int value    ) {
        super(
        );
        this.value = value;
    }


    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }

    public fsm_NumberVariable getFsm_numbervariable() {
        return fsm_numbervariable;
    }

    public void setFsm_numbervariable(fsm_NumberVariable fsm_numbervariable) {
        this.fsm_numbervariable = fsm_numbervariable;
    }

}