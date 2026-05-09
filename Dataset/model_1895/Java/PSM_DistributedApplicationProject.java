





import java.util.List;
import java.util.ArrayList;

public class PSM_DistributedApplicationProject  {

    private String ProjectPackageURL;
    private String ApplicationName;





    private PSM_RootPSM psm_rootpsm;


    public PSM_DistributedApplicationProject(
        String ProjectPackageURL,        String ApplicationName    ) {
        this.ProjectPackageURL = ProjectPackageURL;
        this.ApplicationName = ApplicationName;
    }


    public String getProjectpackageurl() {
        return ProjectPackageURL;
    }

    public void setProjectpackageurl(String ProjectPackageURL) {
        this.ProjectPackageURL = ProjectPackageURL;
    }
    public String getApplicationname() {
        return ApplicationName;
    }

    public void setApplicationname(String ApplicationName) {
        this.ApplicationName = ApplicationName;
    }

    public PSM_RootPSM getPsm_rootpsm() {
        return psm_rootpsm;
    }

    public void setPsm_rootpsm(PSM_RootPSM psm_rootpsm) {
        this.psm_rootpsm = psm_rootpsm;
    }

}