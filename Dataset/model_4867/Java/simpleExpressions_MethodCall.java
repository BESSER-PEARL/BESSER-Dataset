





import java.util.List;
import java.util.ArrayList;

public class simpleExpressions_MethodCall extends Expression {

    private String value;



    public simpleExpressions_MethodCall(
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