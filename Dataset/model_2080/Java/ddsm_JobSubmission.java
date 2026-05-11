





import java.util.List;
import java.util.ArrayList;

public class ddsm_JobSubmission extends CloudElement {

    private String applicationArguments;
    private String mainClass;
    private String artifactUrl;



    public ddsm_JobSubmission(
        String applicationArguments,        String mainClass,        String artifactUrl    ) {
        super(
        );
        this.applicationArguments = applicationArguments;
        this.mainClass = mainClass;
        this.artifactUrl = artifactUrl;
    }


    public String getApplicationarguments() {
        return applicationArguments;
    }

    public void setApplicationarguments(String applicationArguments) {
        this.applicationArguments = applicationArguments;
    }
    public String getMainclass() {
        return mainClass;
    }

    public void setMainclass(String mainClass) {
        this.mainClass = mainClass;
    }
    public String getArtifacturl() {
        return artifactUrl;
    }

    public void setArtifacturl(String artifactUrl) {
        this.artifactUrl = artifactUrl;
    }


}