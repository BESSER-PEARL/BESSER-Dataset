





import java.util.List;
import java.util.ArrayList;

public class diagram_style_EllipseNodeDescription extends NodeStyleDescription {

    private String verticalDiameterComputationExpression;
    private String horizontalDiameterComputationExpression;





    private ColorDescription colordescription;


    public diagram_style_EllipseNodeDescription(
        String verticalDiameterComputationExpression,        String horizontalDiameterComputationExpression    ) {
        super(
        );
        this.verticalDiameterComputationExpression = verticalDiameterComputationExpression;
        this.horizontalDiameterComputationExpression = horizontalDiameterComputationExpression;
    }


    public String getVerticaldiametercomputationexpression() {
        return verticalDiameterComputationExpression;
    }

    public void setVerticaldiametercomputationexpression(String verticalDiameterComputationExpression) {
        this.verticalDiameterComputationExpression = verticalDiameterComputationExpression;
    }
    public String getHorizontaldiametercomputationexpression() {
        return horizontalDiameterComputationExpression;
    }

    public void setHorizontaldiametercomputationexpression(String horizontalDiameterComputationExpression) {
        this.horizontalDiameterComputationExpression = horizontalDiameterComputationExpression;
    }

    public ColorDescription getColordescription() {
        return colordescription;
    }

    public void setColordescription(ColorDescription colordescription) {
        this.colordescription = colordescription;
    }

}