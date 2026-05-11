





import java.util.List;
import java.util.ArrayList;

public class activitydiagram_IntegerValue extends Value, IntegerExpression {

    private int value;



    public activitydiagram_IntegerValue(
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