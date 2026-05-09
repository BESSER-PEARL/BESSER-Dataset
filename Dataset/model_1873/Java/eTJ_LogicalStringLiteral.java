





import java.util.List;
import java.util.ArrayList;

public class eTJ_LogicalStringLiteral extends LogicalExpression {

    private String value;



    public eTJ_LogicalStringLiteral(
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