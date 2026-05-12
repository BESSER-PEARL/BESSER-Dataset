





import java.util.List;
import java.util.ArrayList;

public class build_command_BooleanAdvice extends IAdvise {

    private boolean value;



    public build_command_BooleanAdvice(
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