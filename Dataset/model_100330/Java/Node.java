





import java.util.List;
import java.util.ArrayList;

public class Node  {






    private PNML_ToolSpecific pnml_toolspecific;




    private PNML_Reference pnml_reference;




    private PNML_NetContentElement pnml_netcontentelement;


    public Node(
    ) {
    }



    public PNML_ToolSpecific getPnml_toolspecific() {
        return pnml_toolspecific;
    }

    public void setPnml_toolspecific(PNML_ToolSpecific pnml_toolspecific) {
        this.pnml_toolspecific = pnml_toolspecific;
    }
    public PNML_Reference getPnml_reference() {
        return pnml_reference;
    }

    public void setPnml_reference(PNML_Reference pnml_reference) {
        this.pnml_reference = pnml_reference;
    }
    public PNML_NetContentElement getPnml_netcontentelement() {
        return pnml_netcontentelement;
    }

    public void setPnml_netcontentelement(PNML_NetContentElement pnml_netcontentelement) {
        this.pnml_netcontentelement = pnml_netcontentelement;
    }

}