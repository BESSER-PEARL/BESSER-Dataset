





import java.util.List;
import java.util.ArrayList;

public class cal_AstExpressionInteger extends AstExpressionLiteral {

    private String value;



    public cal_AstExpressionInteger(
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