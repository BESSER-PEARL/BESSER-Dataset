





import java.util.List;
import java.util.ArrayList;

public class core_VerificationActivity extends IdentifiedElement {

    private boolean passed;
    private String verificationMethod;





    private List<core_EObject> core_eobjects;


    public core_VerificationActivity(
        boolean passed,        String verificationMethod    ) {
        super(
        );
        this.passed = passed;
        this.verificationMethod = verificationMethod;
        this.core_eobjects = new ArrayList<>();
    }

    public core_VerificationActivity(
        boolean passed,        String verificationMethod        ArrayList<core_EObject> core_eobjects    ) {
        this.passed = passed;
        this.verificationMethod = verificationMethod;
        this.core_eobjects = core_eobjects;
    }

    public boolean getPassed() {
        return passed;
    }

    public void setPassed(boolean passed) {
        this.passed = passed;
    }
    public String getVerificationmethod() {
        return verificationMethod;
    }

    public void setVerificationmethod(String verificationMethod) {
        this.verificationMethod = verificationMethod;
    }

    public List<core_EObject> getCore_eobjects() {
        return core_eobjects;
    }

    public void addCore_eobject(Core_eobject core_eobject) {
        this.core_eobjects.add(core_eobject);
    }

}