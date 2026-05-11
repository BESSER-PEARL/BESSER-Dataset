





import java.util.List;
import java.util.ArrayList;

public class carnot_DataMappingType extends IIdentifiableElement, IModelElement {

    private String context;
    private String direction;
    private String dataPath;
    private String applicationPath;
    private String applicationAccessPoint;



    public carnot_DataMappingType(
        String context,        String direction,        String dataPath,        String applicationPath,        String applicationAccessPoint    ) {
        super(
        );
        this.context = context;
        this.direction = direction;
        this.dataPath = dataPath;
        this.applicationPath = applicationPath;
        this.applicationAccessPoint = applicationAccessPoint;
    }


    public String getContext() {
        return context;
    }

    public void setContext(String context) {
        this.context = context;
    }
    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }
    public String getDatapath() {
        return dataPath;
    }

    public void setDatapath(String dataPath) {
        this.dataPath = dataPath;
    }
    public String getApplicationpath() {
        return applicationPath;
    }

    public void setApplicationpath(String applicationPath) {
        this.applicationPath = applicationPath;
    }
    public String getApplicationaccesspoint() {
        return applicationAccessPoint;
    }

    public void setApplicationaccesspoint(String applicationAccessPoint) {
        this.applicationAccessPoint = applicationAccessPoint;
    }


}