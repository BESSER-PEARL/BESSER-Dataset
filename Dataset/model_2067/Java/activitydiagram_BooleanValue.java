





import java.util.List;
import java.util.ArrayList;

public class activitydiagram_BooleanValue extends BooleanExpression, Value {

    private boolean value;



    public activitydiagram_BooleanValue(
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