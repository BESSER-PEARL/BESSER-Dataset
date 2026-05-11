





import java.util.List;
import java.util.ArrayList;

public class diagram_style_DotDescription extends NodeStyleDescription {

    private String strokeSizeComputationExpression;



    public diagram_style_DotDescription(
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