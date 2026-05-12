





import java.util.List;
import java.util.ArrayList;

public class query_StringArrayExpression extends ArrayExpression {

    private String values;



    public query_StringArrayExpression(
        String values    ) {
        super(
        );
        this.values = values;
    }


    public String getValues() {
        return values;
    }

    public void setValues(String values) {
        this.values = values;
    }


}