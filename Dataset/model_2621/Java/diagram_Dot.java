





import java.util.List;
import java.util.ArrayList;

public class diagram_Dot extends NodeStyle {

    private String strokeSizeComputationExpression;
    private String backgroundColor;



    public diagram_Dot(
        String strokeSizeComputationExpression,        String backgroundColor    ) {
        super(
        );
        this.strokeSizeComputationExpression = strokeSizeComputationExpression;
        this.backgroundColor = backgroundColor;
    }


    public String getStrokesizecomputationexpression() {
        return strokeSizeComputationExpression;
    }

    public void setStrokesizecomputationexpression(String strokeSizeComputationExpression) {
        this.strokeSizeComputationExpression = strokeSizeComputationExpression;
    }
    public String getBackgroundcolor() {
        return backgroundColor;
    }

    public void setBackgroundcolor(String backgroundColor) {
        this.backgroundColor = backgroundColor;
    }


}