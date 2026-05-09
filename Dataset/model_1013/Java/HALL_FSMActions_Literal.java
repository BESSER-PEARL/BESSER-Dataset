





import java.util.List;
import java.util.ArrayList;

public class HALL_FSMActions_Literal extends ActionExpression {

    private String value;



    public HALL_FSMActions_Literal(
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