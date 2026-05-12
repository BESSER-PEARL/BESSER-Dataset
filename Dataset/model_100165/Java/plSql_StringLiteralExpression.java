





import java.util.List;
import java.util.ArrayList;

public class plSql_StringLiteralExpression extends Expression {

    private String value;



    public plSql_StringLiteralExpression(
        String value    ) {
        super(
        );
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


}