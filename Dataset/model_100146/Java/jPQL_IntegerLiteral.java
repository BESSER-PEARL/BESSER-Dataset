





import java.util.List;
import java.util.ArrayList;

public class jPQL_IntegerLiteral extends Literal {

    private int value;



    public jPQL_IntegerLiteral(
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