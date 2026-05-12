





import java.util.List;
import java.util.ArrayList;

public class YasperEPNML114_ReferencePlaceSpecific  {

    private String tool;
    private String version;





    private YasperEPNML114_NodeGraphics yasperepnml114_nodegraphics;


    public YasperEPNML114_ReferencePlaceSpecific(
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

    public YasperEPNML114_NodeGraphics getYasperepnml114_nodegraphics() {
        return yasperepnml114_nodegraphics;
    }

    public void setYasperepnml114_nodegraphics(YasperEPNML114_NodeGraphics yasperepnml114_nodegraphics) {
        this.yasperepnml114_nodegraphics = yasperepnml114_nodegraphics;
    }

}