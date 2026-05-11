





import java.util.List;
import java.util.ArrayList;

public class cloudml_UploadCommand  {

    private String source;
    private String target;





    private cloudml_Resource cloudml_resource;


    public cloudml_UploadCommand(
        String source,        String target    ) {
        this.source = source;
        this.target = target;
    }


    public String getSource() {
        return source;
    }

    public void setSource(String source) {
        this.source = source;
    }
    public String getTarget() {
        return target;
    }

    public void setTarget(String target) {
        this.target = target;
    }

    public cloudml_Resource getCloudml_resource() {
        return cloudml_resource;
    }

    public void setCloudml_resource(cloudml_Resource cloudml_resource) {
        this.cloudml_resource = cloudml_resource;
    }

}