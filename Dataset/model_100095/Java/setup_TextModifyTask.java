





import java.util.List;
import java.util.ArrayList;

public class setup_TextModifyTask extends SetupTask {

    private String encoding;
    private String uRL;



    public setup_TextModifyTask(
        String encoding,        String uRL    ) {
        super(
        );
        this.encoding = encoding;
        this.uRL = uRL;
    }


    public String getEncoding() {
        return encoding;
    }

    public void setEncoding(String encoding) {
        this.encoding = encoding;
    }
    public String getUrl() {
        return uRL;
    }

    public void setUrl(String uRL) {
        this.uRL = uRL;
    }


}