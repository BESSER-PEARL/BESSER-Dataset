





import java.util.List;
import java.util.ArrayList;

public class tgg_LiteralExpression extends Expression {

    private String value;



    public tgg_LiteralExpression(
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