





import java.util.List;
import java.util.ArrayList;

public class gremlin_IntegerLiteral extends Expression {

    private int value;



    public gremlin_IntegerLiteral(
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