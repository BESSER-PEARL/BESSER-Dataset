





import java.util.List;
import java.util.ArrayList;

public class model_xbase_XConstructorCall extends XExpression {

    private boolean validFeature;
    private String invalidFeatureIssueCode;



    public model_xbase_XConstructorCall(
        boolean validFeature,        String invalidFeatureIssueCode    ) {
        super(
        );
        this.validFeature = validFeature;
        this.invalidFeatureIssueCode = invalidFeatureIssueCode;
    }


    public boolean getValidfeature() {
        return validFeature;
    }

    public void setValidfeature(boolean validFeature) {
        this.validFeature = validFeature;
    }
    public String getInvalidfeatureissuecode() {
        return invalidFeatureIssueCode;
    }

    public void setInvalidfeatureissuecode(String invalidFeatureIssueCode) {
        this.invalidFeatureIssueCode = invalidFeatureIssueCode;
    }


}