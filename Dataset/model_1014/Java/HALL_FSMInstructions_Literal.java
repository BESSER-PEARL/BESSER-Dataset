





import java.util.List;
import java.util.ArrayList;

public class HALL_FSMInstructions_Literal extends PosConditionExpressionElement {

    private String value;



    public HALL_FSMInstructions_Literal(
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