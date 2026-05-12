





import java.util.List;
import java.util.ArrayList;

public class model_ToolInfo  {

    private String tool;
    private String version;





    private model_HasToolInfo model_hastoolinfo;




    private model_HasToolInfo model_hastoolinfo;


    public model_ToolInfo(
        String tool,        String version    ) {
        this.tool = tool;
        this.version = version;
    }


    public String getTool() {
        return tool;
    }

    public void setTool(String tool) {
        this.tool = tool;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }

    public model_HasToolInfo getModel_hastoolinfo() {
        return model_hastoolinfo;
    }

    public void setModel_hastoolinfo(model_HasToolInfo model_hastoolinfo) {
        this.model_hastoolinfo = model_hastoolinfo;
    }
    public model_HasToolInfo getModel_hastoolinfo() {
        return model_hastoolinfo;
    }

    public void setModel_hastoolinfo(model_HasToolInfo model_hastoolinfo) {
        this.model_hastoolinfo = model_hastoolinfo;
    }

}