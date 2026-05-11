





import java.util.List;
import java.util.ArrayList;

public class viewpoint_description_InterpolatedColor extends description_UserColor, description_ColorDescription {

    private String maxValueComputationExpression;
    private String colorValueComputationExpression;
    private String minValueComputationExpression;





    private List<ColorStep> colorsteps;


    public viewpoint_description_InterpolatedColor(
        String maxValueComputationExpression,        String colorValueComputationExpression,        String minValueComputationExpression    ) {
        super(
        );
        this.maxValueComputationExpression = maxValueComputationExpression;
        this.colorValueComputationExpression = colorValueComputationExpression;
        this.minValueComputationExpression = minValueComputationExpression;
        this.colorsteps = new ArrayList<>();
    }

    public viewpoint_description_InterpolatedColor(
        String maxValueComputationExpression,        String colorValueComputationExpression,        String minValueComputationExpression        ArrayList<ColorStep> colorsteps    ) {
        this.maxValueComputationExpression = maxValueComputationExpression;
        this.colorValueComputationExpression = colorValueComputationExpression;
        this.minValueComputationExpression = minValueComputationExpression;
        this.colorsteps = colorsteps;
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
    public String getMinvaluecomputationexpression() {
        return minValueComputationExpression;
    }

    public void setMinvaluecomputationexpression(String minValueComputationExpression) {
        this.minValueComputationExpression = minValueComputationExpression;
    }

    public List<ColorStep> getColorsteps() {
        return colorsteps;
    }

    public void addColorstep(Colorstep colorstep) {
        this.colorsteps.add(colorstep);
    }

}