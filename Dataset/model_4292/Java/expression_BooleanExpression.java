





import java.util.List;
import java.util.ArrayList;

public class expression_BooleanExpression extends SubExpression {

    private String value;



    public expression_BooleanExpression(
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