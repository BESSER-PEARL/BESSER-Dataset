





import java.util.List;
import java.util.ArrayList;

public class YasperEPNML114_ToolspecificType  {

    private String any;
    private String tool;
    private String mixed;
    private String version;
    private String group;





    private YasperEPNML114_Arc yasperepnml114_arc;


    public YasperEPNML114_ToolspecificType(
        String any,        String tool,        String mixed,        String version,        String group    ) {
        this.any = any;
        this.tool = tool;
        this.mixed = mixed;
        this.version = version;
        this.group = group;
    }


    public String getAny() {
        return any;
    }

    public void setAny(String any) {
        this.any = any;
    }
    public String getTool() {
        return tool;
    }

    public void setTool(String tool) {
        this.tool = tool;
    }
    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }

    public YasperEPNML114_Arc getYasperepnml114_arc() {
        return yasperepnml114_arc;
    }

    public void setYasperepnml114_arc(YasperEPNML114_Arc yasperepnml114_arc) {
        this.yasperepnml114_arc = yasperepnml114_arc;
    }

}