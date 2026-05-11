





import java.util.List;
import java.util.ArrayList;

public class viewpoint_description_InterpolatedColor extends description_ColorDescription, description_UserColor {

    private String colorValueComputationExpression;
    private String minValueComputationExpression;
    private String maxValueComputationExpression;



    public viewpoint_description_InterpolatedColor(
        String colorValueComputationExpression,        String minValueComputationExpression,        String maxValueComputationExpression    ) {
        super(
        );
        this.colorValueComputationExpression = colorValueComputationExpression;
        this.minValueComputationExpression = minValueComputationExpression;
        this.maxValueComputationExpression = maxValueComputationExpression;
    }


    public String getColorvaluecomputationexpression() {
        return colorValueComputationExpression;
    }

    public void setColorvaluecomputationexpression(String colorValueComputationExpression) {
        this.colorValueComputationExpression = colorValueComputationExpression;
    }
    public String getMinvaluecomputationexpression() {
        return minValueComputationExpression;
    }

    public void setMinvaluecomputationexpression(String minValueComputationExpression) {
        this.minValueComputationExpression = minValueComputationExpression;
    }
    public String getMaxvaluecomputationexpression() {
        return maxValueComputationExpression;
    }

    public void setMaxvaluecomputationexpression(String maxValueComputationExpression) {
        this.maxValueComputationExpression = maxValueComputationExpression;
    }


}