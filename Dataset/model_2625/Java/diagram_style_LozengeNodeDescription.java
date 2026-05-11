





import java.util.List;
import java.util.ArrayList;

public class diagram_style_LozengeNodeDescription extends NodeStyleDescription {

    private String heightComputationExpression;
    private String widthComputationExpression;





    private ColorDescription colordescription;


    public diagram_style_LozengeNodeDescription(
        String heightComputationExpression,        String widthComputationExpression    ) {
        super(
        );
        this.heightComputationExpression = heightComputationExpression;
        this.widthComputationExpression = widthComputationExpression;
    }


    public String getHeightcomputationexpression() {
        return heightComputationExpression;
    }

    public void setHeightcomputationexpression(String heightComputationExpression) {
        this.heightComputationExpression = heightComputationExpression;
    }
    public String getWidthcomputationexpression() {
        return widthComputationExpression;
    }

    public void setWidthcomputationexpression(String widthComputationExpression) {
        this.widthComputationExpression = widthComputationExpression;
    }

    public ColorDescription getColordescription() {
        return colordescription;
    }

    public void setColordescription(ColorDescription colordescription) {
        this.colordescription = colordescription;
    }

}