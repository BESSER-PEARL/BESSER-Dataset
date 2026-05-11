





import java.util.List;
import java.util.ArrayList;

public class core_VerificationActivity extends IdentifiedElement {

    private boolean passed;
    private String verificationMethod;



    public core_VerificationActivity(
        boolean passed,        String verificationMethod    ) {
        super(
        );
        this.passed = passed;
        this.verificationMethod = verificationMethod;
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


}