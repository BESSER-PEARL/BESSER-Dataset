





import java.util.List;
import java.util.ArrayList;

public class viewpoint_description_InterpolatedColor extends description_ColorDescription, description_UserColor {

    private String minValueComputationExpression;
    private String maxValueComputationExpression;
    private String colorValueComputationExpression;



    public viewpoint_description_InterpolatedColor(
        String minValueComputationExpression,        String maxValueComputationExpression,        String colorValueComputationExpression    ) {
        super(
        );
        this.minValueComputationExpression = minValueComputationExpression;
        this.maxValueComputationExpression = maxValueComputationExpression;
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
    public String getColorvaluecomputationexpression() {
        return colorValueComputationExpression;
    }

    public void setColorvaluecomputationexpression(String colorValueComputationExpression) {
        this.colorValueComputationExpression = colorValueComputationExpression;
    }


}