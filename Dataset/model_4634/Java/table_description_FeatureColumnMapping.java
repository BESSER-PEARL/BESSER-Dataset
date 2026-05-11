





import java.util.List;
import java.util.ArrayList;

public class table_description_FeatureColumnMapping extends description_ColumnMapping, description_StyleUpdater, description_CellUpdater {

    private String featureName;
    private String labelExpression;
    private String featureParentExpression;



    public table_description_FeatureColumnMapping(
        String featureName,        String labelExpression,        String featureParentExpression    ) {
        super(
        );
        this.featureName = featureName;
        this.labelExpression = labelExpression;
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
    public String getFeatureparentexpression() {
        return featureParentExpression;
    }

    public void setFeatureparentexpression(String featureParentExpression) {
        this.featureParentExpression = featureParentExpression;
    }


}