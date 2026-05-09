





import java.util.List;
import java.util.ArrayList;

public class mancoosimm_Configuration extends NamedElement {

    private String creationTime;
    private String systemType;



    public mancoosimm_Configuration(
        String creationTime,        String systemType    ) {
        super(
        );
        this.creationTime = creationTime;
        this.systemType = systemType;
    }


    public String getCreationtime() {
        return creationTime;
    }

    public void setCreationtime(String creationTime) {
        this.creationTime = creationTime;
    }
    public String getSystemtype() {
        return systemType;
    }

    public void setSystemtype(String systemType) {
        this.systemType = systemType;
    }


}