





import java.util.List;
import java.util.ArrayList;

public class setup_Preferences extends ScopeRoot {

    private String installFolder;
    private String acceptedLicenses;



    public setup_Preferences(
        String installFolder,        String acceptedLicenses    ) {
        super(
        );
        this.installFolder = installFolder;
        this.acceptedLicenses = acceptedLicenses;
    }


    public String getInstallfolder() {
        return installFolder;
    }

    public void setInstallfolder(String installFolder) {
        this.installFolder = installFolder;
    }
    public String getAcceptedlicenses() {
        return acceptedLicenses;
    }

    public void setAcceptedlicenses(String acceptedLicenses) {
        this.acceptedLicenses = acceptedLicenses;
    }


}