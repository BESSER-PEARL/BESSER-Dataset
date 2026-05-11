





import java.util.List;
import java.util.ArrayList;

public class arithmetic_NumberLiteral extends Expression {

    private int value;



    public arithmetic_NumberLiteral(
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