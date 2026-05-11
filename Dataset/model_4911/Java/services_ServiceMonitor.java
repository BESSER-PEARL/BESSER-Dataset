





import java.util.List;
import java.util.ArrayList;

public class services_ServiceMonitor extends Base {

    private String revision;
    private String name;



    public services_ServiceMonitor(
        String revision,        String name    ) {
        super(
        );
        this.revision = revision;
        this.name = name;
    }


    public String getRevision() {
        return revision;
    }

    public void setRevision(String revision) {
        this.revision = revision;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}