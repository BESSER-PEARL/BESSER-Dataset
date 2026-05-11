





import java.util.List;
import java.util.ArrayList;

public class mt_expressions_IntegerLiteral extends Literal {

    private int value;



    public mt_expressions_IntegerLiteral(
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