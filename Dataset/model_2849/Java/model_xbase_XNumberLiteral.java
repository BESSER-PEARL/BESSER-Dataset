





import java.util.List;
import java.util.ArrayList;

public class model_xbase_XNumberLiteral extends XExpression {

    private String value;



    public model_xbase_XNumberLiteral(
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