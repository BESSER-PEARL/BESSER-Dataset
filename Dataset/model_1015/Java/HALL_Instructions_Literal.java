





import java.util.List;
import java.util.ArrayList;

public class HALL_Instructions_Literal extends PosConditionMessageExpressionElement {

    private String value;



    public HALL_Instructions_Literal(
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