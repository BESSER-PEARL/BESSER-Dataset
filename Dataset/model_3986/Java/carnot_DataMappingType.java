





import java.util.List;
import java.util.ArrayList;

public class carnot_DataMappingType extends IExtensibleElement, IIdentifiableElement, IModelElement {

    private String applicationAccessPoint;
    private String applicationPath;
    private String context;
    private String dataPath;
    private String direction;



    public carnot_DataMappingType(
        String applicationAccessPoint,        String applicationPath,        String context,        String dataPath,        String direction    ) {
        super(
        );
        this.applicationAccessPoint = applicationAccessPoint;
        this.applicationPath = applicationPath;
        this.context = context;
        this.dataPath = dataPath;
        this.direction = direction;
    }


    public String getApplicationaccesspoint() {
        return applicationAccessPoint;
    }

    public void setApplicationaccesspoint(String applicationAccessPoint) {
        this.applicationAccessPoint = applicationAccessPoint;
    }
    public String getApplicationpath() {
        return applicationPath;
    }

    public void setApplicationpath(String applicationPath) {
        this.applicationPath = applicationPath;
    }
    public String getContext() {
        return context;
    }

    public void setContext(String context) {
        this.context = context;
    }
    public String getDatapath() {
        return dataPath;
    }

    public void setDatapath(String dataPath) {
        this.dataPath = dataPath;
    }
    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }


}