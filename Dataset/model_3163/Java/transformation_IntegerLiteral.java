





import java.util.List;
import java.util.ArrayList;

public class transformation_IntegerLiteral extends Expression {

    private int value;



    public transformation_IntegerLiteral(
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