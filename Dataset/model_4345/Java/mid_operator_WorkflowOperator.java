





import java.util.List;
import java.util.ArrayList;

public class mid_operator_WorkflowOperator extends Operator {

    private String midUri;



    public mid_operator_WorkflowOperator(
        String midUri    ) {
        super(
        );
        this.midUri = midUri;
    }


    public String getMiduri() {
        return midUri;
    }

    public void setMiduri(String midUri) {
        this.midUri = midUri;
    }


}