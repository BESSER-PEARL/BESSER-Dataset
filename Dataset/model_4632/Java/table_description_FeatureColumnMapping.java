





import java.util.List;
import java.util.ArrayList;

public class table_description_FeatureColumnMapping extends description_CellUpdater, description_StyleUpdater, description_ColumnMapping {

    private String featureParentExpression;
    private String labelExpression;
    private String featureName;



    public table_description_FeatureColumnMapping(
        String featureParentExpression,        String labelExpression,        String featureName    ) {
        super(
        );
        this.featureParentExpression = featureParentExpression;
        this.labelExpression = labelExpression;
        this.featureName = featureName;
    }


    public String getFeatureparentexpression() {
        return featureParentExpression;
    }

    public void setFeatureparentexpression(String featureParentExpression) {
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


}