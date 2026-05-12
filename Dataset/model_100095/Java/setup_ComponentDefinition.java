





import java.util.List;
import java.util.ArrayList;

public class setup_ComponentDefinition extends ComponentExtension {

    private String version;
    private String iD;



    public setup_ComponentDefinition(
        String version,        String iD    ) {
        super(
        );
        this.version = version;
        this.iD = iD;
    }


    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getId() {
        return iD;
    }

    public void setId(String iD) {
        this.iD = iD;
    }


}