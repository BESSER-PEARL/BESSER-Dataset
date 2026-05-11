





import java.util.List;
import java.util.ArrayList;

public class co2_NumberLiteral extends Expression {

    private int value;



    public co2_NumberLiteral(
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