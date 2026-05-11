





import java.util.List;
import java.util.ArrayList;

public class mathInterpreter_Num extends Expression {

    private int value;



    public mathInterpreter_Num(
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