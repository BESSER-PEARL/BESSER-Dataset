





import java.util.List;
import java.util.ArrayList;

public class sourcecleaner_Schema extends Source {

    private String extensionName;
    private String extensionId;
    private String pluginName;





    private sourcecleaner_Project sourcecleaner_project;




    private sourcecleaner_Project sourcecleaner_project;


    public sourcecleaner_Schema(
        String extensionName,        String extensionId,        String pluginName    ) {
        super(
        );
        this.extensionName = extensionName;
        this.extensionId = extensionId;
        this.pluginName = pluginName;
    }


    public String getExtensionname() {
        return extensionName;
    }

    public void setExtensionname(String extensionName) {
        this.extensionName = extensionName;
    }
    public String getExtensionid() {
        return extensionId;
    }

    public void setExtensionid(String extensionId) {
        this.extensionId = extensionId;
    }
    public String getPluginname() {
        return pluginName;
    }

    public void setPluginname(String pluginName) {
        this.pluginName = pluginName;
    }

    public sourcecleaner_Project getSourcecleaner_project() {
        return sourcecleaner_project;
    }

    public void setSourcecleaner_project(sourcecleaner_Project sourcecleaner_project) {
        this.sourcecleaner_project = sourcecleaner_project;
    }
    public sourcecleaner_Project getSourcecleaner_project() {
        return sourcecleaner_project;
    }

    public void setSourcecleaner_project(sourcecleaner_Project sourcecleaner_project) {
        this.sourcecleaner_project = sourcecleaner_project;
    }

}