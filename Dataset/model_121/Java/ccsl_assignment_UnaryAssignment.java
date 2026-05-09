





import java.util.List;
import java.util.ArrayList;

public class ccsl_assignment_UnaryAssignment extends AbstractAssignment {

    private String operator;



    public ccsl_assignment_UnaryAssignment(
        String operator    ) {
        super(
        );
        this.operator = operator;
    }


    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }


}