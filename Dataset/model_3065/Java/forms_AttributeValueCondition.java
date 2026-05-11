





import java.util.List;
import java.util.ArrayList;

public class forms_AttributeValueCondition extends Condition {

    private String value;



    public forms_AttributeValueCondition(
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