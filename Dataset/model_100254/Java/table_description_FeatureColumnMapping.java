





import java.util.List;
import java.util.ArrayList;

public class table_description_FeatureColumnMapping extends description_CellUpdater, description_ColumnMapping, description_StyleUpdater {

    private String featureParentExpression;
    private String featureName;
    private String labelExpression;



    public table_description_FeatureColumnMapping(
        String featureParentExpression,        String featureName,        String labelExpression    ) {
        super(
        );
        this.featureParentExpression = featureParentExpression;
        this.featureName = featureName;
        this.labelExpression = labelExpression;
    }


    public String getFeatureparentexpression() {
        return featureParentExpression;
    }

    public void setFeatureparentexpression(String featureParentExpression) {
        this.featureParentExpression = featureParentExpression;
    }
    public String getFeaturename() {
        return featureName;
    }

    public void setFeaturename(String featureName) {
        this.featureName = featureName;
    }
    public String getLabelexpression() {
        return labelExpression;
    }

    public void setLabelexpression(String labelExpression) {
        this.labelExpression = labelExpression;
    }


}