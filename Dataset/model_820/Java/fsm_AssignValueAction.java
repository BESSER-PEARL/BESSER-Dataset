





import java.util.List;
import java.util.ArrayList;

public class fsm_AssignValueAction extends Action {

    private boolean value;



    public fsm_AssignValueAction(
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


}