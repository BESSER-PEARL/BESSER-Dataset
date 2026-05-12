





import java.util.List;
import java.util.ArrayList;

public class PNML_ToolSpecific  {

    private String version;
    private String tool;





    private Page page;




    private NetElement netelement;


    public PNML_ToolSpecific(
        String version,        String tool    ) {
        this.version = version;
        this.tool = tool;
    }


    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getTool() {
        return tool;
    }

    public void setTool(String tool) {
        this.tool = tool;
    }

    public Page getPage() {
        return page;
    }

    public void setPage(Page page) {
        this.page = page;
    }
    public NetElement getNetelement() {
        return netelement;
    }

    public void setNetelement(NetElement netelement) {
        this.netelement = netelement;
    }

}