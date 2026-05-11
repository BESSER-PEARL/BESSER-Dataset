





import java.util.List;
import java.util.ArrayList;

public class plSql_IntLiteralExpression extends Expression {

    private int value;



    public plSql_IntLiteralExpression(
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