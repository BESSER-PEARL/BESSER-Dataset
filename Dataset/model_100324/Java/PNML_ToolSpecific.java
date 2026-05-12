





import java.util.List;
import java.util.ArrayList;

public class PNML_ToolSpecific  {

    private String tool;
    private String version;





    private Node node;




    private NetElement netelement;




    private Page page;


    public PNML_ToolSpecific(
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

    public Node getNode() {
        return node;
    }

    public void setNode(Node node) {
        this.node = node;
    }
    public NetElement getNetelement() {
        return netelement;
    }

    public void setNetelement(NetElement netelement) {
        this.netelement = netelement;
    }
    public Page getPage() {
        return page;
    }

    public void setPage(Page page) {
        this.page = page;
    }

}