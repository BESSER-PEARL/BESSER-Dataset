





import java.util.List;
import java.util.ArrayList;

public class sequence_template_TExecutionStyle extends TTransformer {

    private String borderSizeComputationExpression;



    public sequence_template_TExecutionStyle(
        String borderSizeComputationExpression    ) {
        super(
        );
        this.borderSizeComputationExpression = borderSizeComputationExpression;
    }


    public String getBordersizecomputationexpression() {
        return borderSizeComputationExpression;
    }

    public void setBordersizecomputationexpression(String borderSizeComputationExpression) {
        this.borderSizeComputationExpression = borderSizeComputationExpression;
    }


}