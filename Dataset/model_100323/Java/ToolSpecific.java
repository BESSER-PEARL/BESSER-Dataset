





import java.util.List;
import java.util.ArrayList;

public class ToolSpecific  {






    private PNML_Arc pnml_arc;




    private PNML_Node pnml_node;




    private PNML_NetElement pnml_netelement;


    public ToolSpecific(
    ) {
    }



    public PNML_Arc getPnml_arc() {
        return pnml_arc;
    }

    public void setPnml_arc(PNML_Arc pnml_arc) {
        this.pnml_arc = pnml_arc;
    }
    public PNML_Node getPnml_node() {
        return pnml_node;
    }

    public void setPnml_node(PNML_Node pnml_node) {
        this.pnml_node = pnml_node;
    }
    public PNML_NetElement getPnml_netelement() {
        return pnml_netelement;
    }

    public void setPnml_netelement(PNML_NetElement pnml_netelement) {
        this.pnml_netelement = pnml_netelement;
    }

}