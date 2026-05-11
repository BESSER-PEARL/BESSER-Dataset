





import java.util.List;
import java.util.ArrayList;

public class carnot_DataMappingType extends IModelElement, IIdentifiableElement {

    private String direction;
    private String applicationPath;
    private String applicationAccessPoint;
    private String dataPath;
    private String context;



    public carnot_DataMappingType(
        String direction,        String applicationPath,        String applicationAccessPoint,        String dataPath,        String context    ) {
        super(
        );
        this.direction = direction;
        this.applicationPath = applicationPath;
        this.applicationAccessPoint = applicationAccessPoint;
        this.dataPath = dataPath;
        this.context = context;
    }


    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
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
    public String getDatapath() {
        return dataPath;
    }

    public void setDatapath(String dataPath) {
        this.dataPath = dataPath;
    }
    public String getContext() {
        return context;
    }

    public void setContext(String context) {
        this.context = context;
    }


}