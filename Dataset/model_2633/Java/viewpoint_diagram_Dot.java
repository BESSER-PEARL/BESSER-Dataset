





import java.util.List;
import java.util.ArrayList;

public class viewpoint_diagram_Dot extends NodeStyle {

    private String strokeSizeComputationExpression;



    public viewpoint_diagram_Dot(
        String strokeSizeComputationExpression    ) {
        super(
        );
        this.strokeSizeComputationExpression = strokeSizeComputationExpression;
    }


    public String getStrokesizecomputationexpression() {
        return strokeSizeComputationExpression;
    }

    public void setStrokesizecomputationexpression(String strokeSizeComputationExpression) {
        this.strokeSizeComputationExpression = strokeSizeComputationExpression;
    }


}