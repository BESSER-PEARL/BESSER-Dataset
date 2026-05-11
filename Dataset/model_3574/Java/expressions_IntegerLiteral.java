





import java.util.List;
import java.util.ArrayList;

public class expressions_IntegerLiteral extends Expression {

    private int value;



    public expressions_IntegerLiteral(
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