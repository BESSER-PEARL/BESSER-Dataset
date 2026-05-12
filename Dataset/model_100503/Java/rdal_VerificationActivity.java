





import java.util.List;
import java.util.ArrayList;

public class rdal_VerificationActivity extends IdentifiedElement {

    private boolean passed;



    public rdal_VerificationActivity(
        boolean passed    ) {
        super(
        );
        this.passed = passed;
    }


    public boolean getPassed() {
        return passed;
    }

    public void setPassed(boolean passed) {
        this.passed = passed;
    }


}