





import java.util.List;
import java.util.ArrayList;

public class setup_ResourceCreationTask extends SetupTask {

    private String content;
    private String targetURL;
    private String encoding;



    public setup_ResourceCreationTask(
        String content,        String targetURL,        String encoding    ) {
        super(
        );
        this.content = content;
        this.targetURL = targetURL;
        this.encoding = encoding;
    }


    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }
    public String getTargeturl() {
        return targetURL;
    }

    public void setTargeturl(String targetURL) {
        this.targetURL = targetURL;
    }
    public String getEncoding() {
        return encoding;
    }

    public void setEncoding(String encoding) {
        this.encoding = encoding;
    }


}