





import java.util.List;
import java.util.ArrayList;

public class diagram_style_SizeComputationContainerStyleDescription  {

    private String widthComputationExpression;
    private String heightComputationExpression;



    public diagram_style_SizeComputationContainerStyleDescription(
        String widthComputationExpression,        String heightComputationExpression    ) {
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


}