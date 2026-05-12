





import java.util.List;
import java.util.ArrayList;

public class releng_BuildJob  {

    private String sourceBranch;
    private String buckminsterComponent;
    private String types;
    private String name;





    private releng_Server releng_server;


    public releng_BuildJob(
        String sourceBranch,        String buckminsterComponent,        String types,        String name    ) {
        this.sourceBranch = sourceBranch;
        this.buckminsterComponent = buckminsterComponent;
        this.types = types;
        this.name = name;
    }


    public String getSourcebranch() {
        return sourceBranch;
    }

    public void setSourcebranch(String sourceBranch) {
        this.sourceBranch = sourceBranch;
    }
    public String getBuckminstercomponent() {
        return buckminsterComponent;
    }

    public void setBuckminstercomponent(String buckminsterComponent) {
        this.buckminsterComponent = buckminsterComponent;
    }
    public String getTypes() {
        return types;
    }

    public void setTypes(String types) {
        this.types = types;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public releng_Server getReleng_server() {
        return releng_server;
    }

    public void setReleng_server(releng_Server releng_server) {
        this.releng_server = releng_server;
    }

}