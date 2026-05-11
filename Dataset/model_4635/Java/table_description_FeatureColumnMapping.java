





import java.util.List;
import java.util.ArrayList;

public class table_description_FeatureColumnMapping extends description_CellUpdater, description_StyleUpdater, description_ColumnMapping {

    private String labelExpression;
    private String featureName;
    private String featureParentExpression;



    public table_description_FeatureColumnMapping(
        String labelExpression,        String featureName,        String featureParentExpression    ) {
        super(
        );
        this.labelExpression = labelExpression;
        this.featureName = featureName;
        this.featureParentExpression = featureParentExpression;
    }


    public String getLabelexpression() {
        return labelExpression;
    }

    public void setLabelexpression(String labelExpression) {
        this.labelExpression = labelExpression;
    }
    public String getFeaturename() {
        return featureName;
    }

    public void setFeaturename(String featureName) {
        this.featureName = featureName;
    }
    public String getFeatureparentexpression() {
        return featureParentExpression;
    }

    public void setFeatureparentexpression(String featureParentExpression) {
        this.featureParentExpression = featureParentExpression;
    }


}