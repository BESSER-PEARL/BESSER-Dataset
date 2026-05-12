





import java.util.List;
import java.util.ArrayList;

public class timedAutomata_expressions_ConstantExpression extends Expression {

    private int value;



    public timedAutomata_expressions_ConstantExpression(
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