





import java.util.List;
import java.util.ArrayList;

public class boa_EvalBoolRes extends EvalRes {

    private boolean value;



    public boa_EvalBoolRes(
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