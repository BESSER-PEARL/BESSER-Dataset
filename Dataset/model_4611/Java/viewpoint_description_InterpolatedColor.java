





import java.util.List;
import java.util.ArrayList;

public class viewpoint_description_InterpolatedColor extends description_UserColor, description_ColorDescription {

    private String minValueComputationExpression;
    private String colorValueComputationExpression;
    private String maxValueComputationExpression;



    public viewpoint_description_InterpolatedColor(
        String minValueComputationExpression,        String colorValueComputationExpression,        String maxValueComputationExpression    ) {
        super(
        );
        this.minValueComputationExpression = minValueComputationExpression;
        this.colorValueComputationExpression = colorValueComputationExpression;
        this.maxValueComputationExpression = maxValueComputationExpression;
    }


    public String getMinvaluecomputationexpression() {
        return minValueComputationExpression;
    }

    public void setMinvaluecomputationexpression(String minValueComputationExpression) {
        this.minValueComputationExpression = minValueComputationExpression;
    }
    public String getColorvaluecomputationexpression() {
        return colorValueComputationExpression;
    }

    public void setColorvaluecomputationexpression(String colorValueComputationExpression) {
        this.colorValueComputationExpression = colorValueComputationExpression;
    }
    public String getMaxvaluecomputationexpression() {
        return maxValueComputationExpression;
    }

    public void setMaxvaluecomputationexpression(String maxValueComputationExpression) {
        this.maxValueComputationExpression = maxValueComputationExpression;
    }


}