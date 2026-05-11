





import java.util.List;
import java.util.ArrayList;

public class smallJava_SJIntConstant extends SJExpression {

    private int value;



    public smallJava_SJIntConstant(
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