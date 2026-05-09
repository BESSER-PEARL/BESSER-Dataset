





import java.util.List;
import java.util.ArrayList;

public class mancoosimm_Configuration extends NamedElement {

    private String systemType;
    private String creationTime;



    public mancoosimm_Configuration(
        String systemType,        String creationTime    ) {
        super(
        );
        this.systemType = systemType;
        this.creationTime = creationTime;
    }


    public String getSystemtype() {
        return systemType;
    }

    public void setSystemtype(String systemType) {
        this.systemType = systemType;
    }
    public String getCreationtime() {
        return creationTime;
    }

    public void setCreationtime(String creationTime) {
        this.creationTime = creationTime;
    }


}