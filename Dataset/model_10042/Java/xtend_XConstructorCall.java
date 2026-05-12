





import java.util.List;
import java.util.ArrayList;

public class xtend_XConstructorCall extends XExpression {

    private boolean validFeature;
    private String invalidFeatureIssueCode;





    private List<xtend_JvmTypeReference> xtend_jvmtypereferences;




    private xtend_AnonymousClass xtend_anonymousclass;


    public xtend_XConstructorCall(
        boolean validFeature,        String invalidFeatureIssueCode    ) {
        super(
        );
        this.validFeature = validFeature;
        this.invalidFeatureIssueCode = invalidFeatureIssueCode;
        this.xtend_jvmtypereferences = new ArrayList<>();
    }

    public xtend_XConstructorCall(
        boolean validFeature,        String invalidFeatureIssueCode        ArrayList<xtend_JvmTypeReference> xtend_jvmtypereferences    ) {
        this.validFeature = validFeature;
        this.invalidFeatureIssueCode = invalidFeatureIssueCode;
        this.xtend_jvmtypereferences = xtend_jvmtypereferences;
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

    public List<xtend_JvmTypeReference> getXtend_jvmtypereferences() {
        return xtend_jvmtypereferences;
    }

    public void addXtend_jvmtypereference(Xtend_jvmtypereference xtend_jvmtypereference) {
        this.xtend_jvmtypereferences.add(xtend_jvmtypereference);
    }
    public xtend_AnonymousClass getXtend_anonymousclass() {
        return xtend_anonymousclass;
    }

    public void setXtend_anonymousclass(xtend_AnonymousClass xtend_anonymousclass) {
        this.xtend_anonymousclass = xtend_anonymousclass;
    }

}