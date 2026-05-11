





import java.util.List;
import java.util.ArrayList;

public class plsql_expression_ArithmeticExpression extends Expression {

    private String type;



    public plsql_expression_ArithmeticExpression(
        String type    ) {
        super(
        );
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}