





import java.util.List;
import java.util.ArrayList;

public class diagram_style_EllipseNodeDescription extends NodeStyleDescription {

    private String horizontalDiameterComputationExpression;
    private String verticalDiameterComputationExpression;



    public diagram_style_EllipseNodeDescription(
        String horizontalDiameterComputationExpression,        String verticalDiameterComputationExpression    ) {
        super(
        );
        this.horizontalDiameterComputationExpression = horizontalDiameterComputationExpression;
        this.verticalDiameterComputationExpression = verticalDiameterComputationExpression;
    }


    public String getHorizontaldiametercomputationexpression() {
        return horizontalDiameterComputationExpression;
    }

    public void setHorizontaldiametercomputationexpression(String horizontalDiameterComputationExpression) {
        this.horizontalDiameterComputationExpression = horizontalDiameterComputationExpression;
    }
    public String getVerticaldiametercomputationexpression() {
        return verticalDiameterComputationExpression;
    }

    public void setVerticaldiametercomputationexpression(String verticalDiameterComputationExpression) {
        this.verticalDiameterComputationExpression = verticalDiameterComputationExpression;
    }


}