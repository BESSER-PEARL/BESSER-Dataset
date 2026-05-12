





import java.util.List;
import java.util.ArrayList;

public class setup_RedirectionTask extends SetupTask {

    private String sourceURL;
    private String targetURL;



    public setup_RedirectionTask(
        String sourceURL,        String targetURL    ) {
        super(
        );
        this.sourceURL = sourceURL;
        this.targetURL = targetURL;
    }


    public String getSourceurl() {
        return sourceURL;
    }

    public void setSourceurl(String sourceURL) {
        this.sourceURL = sourceURL;
    }
    public String getTargeturl() {
        return targetURL;
    }

    public void setTargeturl(String targetURL) {
        this.targetURL = targetURL;
    }


}