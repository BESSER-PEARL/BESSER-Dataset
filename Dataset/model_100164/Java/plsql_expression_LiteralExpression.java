





import java.util.List;
import java.util.ArrayList;

public class plsql_expression_LiteralExpression extends Expression {

    private String type;
    private String value;



    public plsql_expression_LiteralExpression(
        String type,        String value    ) {
        super(
        );
        this.type = type;
        this.value = value;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


}