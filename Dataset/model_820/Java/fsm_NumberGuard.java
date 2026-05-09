





import java.util.List;
import java.util.ArrayList;

public class fsm_NumberGuard extends Guard {

    private boolean value;



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


}