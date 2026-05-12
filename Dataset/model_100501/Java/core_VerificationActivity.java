





import java.util.List;
import java.util.ArrayList;

public class core_VerificationActivity extends IdentifiedElement {

    private String verificationMethod;
    private boolean passed;



    public core_VerificationActivity(
        String verificationMethod,        boolean passed    ) {
        super(
        );
        this.verificationMethod = verificationMethod;
        this.passed = passed;
    }


    public String getVerificationmethod() {
        return verificationMethod;
    }

    public void setVerificationmethod(String verificationMethod) {
        this.verificationMethod = verificationMethod;
    }
    public boolean getPassed() {
        return passed;
    }

    public void setPassed(boolean passed) {
        this.passed = passed;
    }


}