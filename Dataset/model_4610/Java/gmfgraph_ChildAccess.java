





import java.util.List;
import java.util.ArrayList;

public class gmfgraph_ChildAccess  {

    private String accessor;





    private gmfgraph_Node gmfgraph_node;


    public gmfgraph_ChildAccess(
        String accessor    ) {
        this.accessor = accessor;
    }


    public String getAccessor() {
        return accessor;
    }

    public void setAccessor(String accessor) {
        this.accessor = accessor;
    }

    public gmfgraph_Node getGmfgraph_node() {
        return gmfgraph_node;
    }

    public void setGmfgraph_node(gmfgraph_Node gmfgraph_node) {
        this.gmfgraph_node = gmfgraph_node;
    }

}