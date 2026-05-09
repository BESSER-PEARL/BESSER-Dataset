





import java.util.List;
import java.util.ArrayList;

public class trace_M2CTraceItem extends TraceItem {

    private String targetFile;
    private String token;



    public trace_M2CTraceItem(
        String targetFile,        String token    ) {
        super(
        );
        this.targetFile = targetFile;
        this.token = token;
    }


    public String getTargetfile() {
        return targetFile;
    }

    public void setTargetfile(String targetFile) {
        this.targetFile = targetFile;
    }
    public String getToken() {
        return token;
    }

    public void setToken(String token) {
        this.token = token;
    }


}