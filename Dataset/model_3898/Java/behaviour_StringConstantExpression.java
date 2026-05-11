





import java.util.List;
import java.util.ArrayList;

public class behaviour_StringConstantExpression extends ConstantExpression {

    private String value;



    public behaviour_StringConstantExpression(
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