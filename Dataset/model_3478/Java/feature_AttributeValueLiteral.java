





import java.util.List;
import java.util.ArrayList;

public class feature_AttributeValueLiteral extends AttributeOperand {

    private String value;



    public feature_AttributeValueLiteral(
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