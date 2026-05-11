





import java.util.List;
import java.util.ArrayList;

public class jcl_literals_IntegerLiteral extends literals_Literal, expressions_PrimaryExpression, conditions_ReturnCode {

    private int value;



    public jcl_literals_IntegerLiteral(
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