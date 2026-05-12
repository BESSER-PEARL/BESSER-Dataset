





import java.util.List;
import java.util.ArrayList;

public class setup_ProjectSetImportTask extends SetupTask {

    private String uRL;



    public setup_ProjectSetImportTask(
        String uRL    ) {
        super(
        );
        this.uRL = uRL;
    }


    public String getUrl() {
        return uRL;
    }

    public void setUrl(String uRL) {
        this.uRL = uRL;
    }


}