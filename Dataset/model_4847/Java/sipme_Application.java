





import java.util.List;
import java.util.ArrayList;

public class sipme_Application extends EnterpriseResource {

    private String applicationMaintainer;
    private String applicationEditor;



    public sipme_Application(
        String applicationMaintainer,        String applicationEditor    ) {
        super(
        );
        this.applicationMaintainer = applicationMaintainer;
        this.applicationEditor = applicationEditor;
    }


    public String getApplicationmaintainer() {
        return applicationMaintainer;
    }

    public void setApplicationmaintainer(String applicationMaintainer) {
        this.applicationMaintainer = applicationMaintainer;
    }
    public String getApplicationeditor() {
        return applicationEditor;
    }

    public void setApplicationeditor(String applicationEditor) {
        this.applicationEditor = applicationEditor;
    }


}