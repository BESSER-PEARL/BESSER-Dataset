





import java.util.List;
import java.util.ArrayList;

public class viewpoint_style_LozengeNodeDescription extends NodeStyleDescription {

    private String widthComputationExpression;
    private String heightComputationExpression;





    private ColorDescription colordescription;


    public viewpoint_style_LozengeNodeDescription(
        String widthComputationExpression,        String heightComputationExpression    ) {
        super(
        );
        this.widthComputationExpression = widthComputationExpression;
        this.heightComputationExpression = heightComputationExpression;
    }


    public String getWidthcomputationexpression() {
        return widthComputationExpression;
    }

    public void setWidthcomputationexpression(String widthComputationExpression) {
        this.widthComputationExpression = widthComputationExpression;
    }
    public String getHeightcomputationexpression() {
        return heightComputationExpression;
    }

    public void setHeightcomputationexpression(String heightComputationExpression) {
        this.heightComputationExpression = heightComputationExpression;
    }

    public ColorDescription getColordescription() {
        return colordescription;
    }

    public void setColordescription(ColorDescription colordescription) {
        this.colordescription = colordescription;
    }

}