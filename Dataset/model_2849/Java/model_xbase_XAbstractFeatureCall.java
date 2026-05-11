





import java.util.List;
import java.util.ArrayList;

public class model_xbase_XAbstractFeatureCall extends XExpression {

    private String invalidFeatureIssueCode;
    private boolean validFeature;



    public model_xbase_XAbstractFeatureCall(
        String invalidFeatureIssueCode,        boolean validFeature    ) {
        super(
        );
        this.invalidFeatureIssueCode = invalidFeatureIssueCode;
        this.validFeature = validFeature;
    }


    public String getInvalidfeatureissuecode() {
        return invalidFeatureIssueCode;
    }

    public void setInvalidfeatureissuecode(String invalidFeatureIssueCode) {
        this.invalidFeatureIssueCode = invalidFeatureIssueCode;
    }
    public boolean getValidfeature() {
        return validFeature;
    }

    public void setValidfeature(boolean validFeature) {
        this.validFeature = validFeature;
    }


}