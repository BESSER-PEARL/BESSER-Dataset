





import java.util.List;
import java.util.ArrayList;

public class sequence_template_TLifelineStyle extends TTransformer {

    private String lifelineWidthComputationExpression;



    public sequence_template_TLifelineStyle(
        String lifelineWidthComputationExpression    ) {
        super(
        );
        this.lifelineWidthComputationExpression = lifelineWidthComputationExpression;
    }


    public String getLifelinewidthcomputationexpression() {
        return lifelineWidthComputationExpression;
    }

    public void setLifelinewidthcomputationexpression(String lifelineWidthComputationExpression) {
        this.lifelineWidthComputationExpression = lifelineWidthComputationExpression;
    }


}