





import java.util.List;
import java.util.ArrayList;

public class eol_expression_StringExpression extends ComparableExpression, SummableExpression {

    private String value;



    public eol_expression_StringExpression(
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