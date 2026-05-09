





import java.util.List;
import java.util.ArrayList;

public class fsm_NumberGuard extends Guard {

    private int value;



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


}