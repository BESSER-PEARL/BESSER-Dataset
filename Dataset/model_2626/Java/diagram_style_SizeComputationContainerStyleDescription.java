





import java.util.List;
import java.util.ArrayList;

public class diagram_style_SizeComputationContainerStyleDescription  {

    private String heightComputationExpression;
    private String widthComputationExpression;



    public diagram_style_SizeComputationContainerStyleDescription(
        String heightComputationExpression,        String widthComputationExpression    ) {
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


}