





import java.util.List;
import java.util.ArrayList;

public class SPL_BooleanConstant extends Constant {

    private boolean value;



    public SPL_BooleanConstant(
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