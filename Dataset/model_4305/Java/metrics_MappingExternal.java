





import java.util.List;
import java.util.ArrayList;

public class metrics_MappingExternal extends Mapping {

    private String classURI;
    private String pluginID;



    public metrics_MappingExternal(
        String classURI,        String pluginID    ) {
        super(
        );
        this.classURI = classURI;
        this.pluginID = pluginID;
    }


    public String getClassuri() {
        return classURI;
    }

    public void setClassuri(String classURI) {
        this.classURI = classURI;
    }
    public String getPluginid() {
        return pluginID;
    }

    public void setPluginid(String pluginID) {
        this.pluginID = pluginID;
    }


}