





import java.util.List;
import java.util.ArrayList;

public class ecdarText_ETBooleanLiteral extends ETExpression {

    private String value;



    public ecdarText_ETBooleanLiteral(
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