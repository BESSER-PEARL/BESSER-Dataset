





import java.util.List;
import java.util.ArrayList;

public class viewpoint_style_BorderedStyleDescription extends StyleDescription {

    private String borderSizeComputationExpression;





    private ColorDescription colordescription;


    public viewpoint_style_BorderedStyleDescription(
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

    public ColorDescription getColordescription() {
        return colordescription;
    }

    public void setColordescription(ColorDescription colordescription) {
        this.colordescription = colordescription;
    }

}