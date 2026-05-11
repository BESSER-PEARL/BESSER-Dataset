





import java.util.List;
import java.util.ArrayList;

public class diagram_style_BorderedStyleDescription extends StyleDescription {

    private String borderSizeComputationExpression;



    public diagram_style_BorderedStyleDescription(
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