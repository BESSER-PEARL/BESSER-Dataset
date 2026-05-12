





import java.util.List;
import java.util.ArrayList;

public class setup_P2Task extends SetupTask {

    private boolean mergeDisabled;
    private boolean licenseConfirmationDisabled;



    public setup_P2Task(
        boolean mergeDisabled,        boolean licenseConfirmationDisabled    ) {
        super(
        );
        this.mergeDisabled = mergeDisabled;
        this.licenseConfirmationDisabled = licenseConfirmationDisabled;
    }


    public boolean getMergedisabled() {
        return mergeDisabled;
    }

    public void setMergedisabled(boolean mergeDisabled) {
        this.mergeDisabled = mergeDisabled;
    }
    public boolean getLicenseconfirmationdisabled() {
        return licenseConfirmationDisabled;
    }

    public void setLicenseconfirmationdisabled(boolean licenseConfirmationDisabled) {
        this.licenseConfirmationDisabled = licenseConfirmationDisabled;
    }


}