





import java.util.List;
import java.util.ArrayList;

public class setup_ResourceCopyTask extends SetupTask {

    private String targetURL;
    private String sourceURL;



    public setup_ResourceCopyTask(
        String targetURL,        String sourceURL    ) {
        super(
        );
        this.targetURL = targetURL;
        this.sourceURL = sourceURL;
    }


    public String getTargeturl() {
        return targetURL;
    }

    public void setTargeturl(String targetURL) {
        this.targetURL = targetURL;
    }
    public String getSourceurl() {
        return sourceURL;
    }

    public void setSourceurl(String sourceURL) {
        this.sourceURL = sourceURL;
    }


}