





import java.util.List;
import java.util.ArrayList;

public class cal_ExpressionString extends ExpressionLiteral {

    private String value;



    public cal_ExpressionString(
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