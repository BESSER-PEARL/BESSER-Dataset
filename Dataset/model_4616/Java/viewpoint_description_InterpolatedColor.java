





import java.util.List;
import java.util.ArrayList;

public class viewpoint_description_InterpolatedColor extends description_ColorDescription, description_UserColor {

    private String colorValueComputationExpression;
    private String maxValueComputationExpression;
    private String minValueComputationExpression;



    public viewpoint_description_InterpolatedColor(
        String colorValueComputationExpression,        String maxValueComputationExpression,        String minValueComputationExpression    ) {
        super(
        );
        this.colorValueComputationExpression = colorValueComputationExpression;
        this.maxValueComputationExpression = maxValueComputationExpression;
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
    public String getMinvaluecomputationexpression() {
        return minValueComputationExpression;
    }

    public void setMinvaluecomputationexpression(String minValueComputationExpression) {
        this.minValueComputationExpression = minValueComputationExpression;
    }


}