





import java.util.List;
import java.util.ArrayList;

public class diagram_Dot extends NodeStyle {

    private String backgroundColor;
    private String strokeSizeComputationExpression;



    public diagram_Dot(
        String backgroundColor,        String strokeSizeComputationExpression    ) {
        super(
        );
        this.backgroundColor = backgroundColor;
        this.strokeSizeComputationExpression = strokeSizeComputationExpression;
    }


    public String getBackgroundcolor() {
        return backgroundColor;
    }

    public void setBackgroundcolor(String backgroundColor) {
        this.backgroundColor = backgroundColor;
    }
    public String getStrokesizecomputationexpression() {
        return strokeSizeComputationExpression;
    }

    public void setStrokesizecomputationexpression(String strokeSizeComputationExpression) {
        this.strokeSizeComputationExpression = strokeSizeComputationExpression;
    }


}