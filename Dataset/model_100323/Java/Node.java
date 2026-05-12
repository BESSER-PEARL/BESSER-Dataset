





import java.util.List;
import java.util.ArrayList;

public class Node  {






    private PNML_NetContentElement pnml_netcontentelement;




    private PNML_NodeGraphics pnml_nodegraphics;


    public Node(
    ) {
    }



    public PNML_NetContentElement getPnml_netcontentelement() {
        return pnml_netcontentelement;
    }

    public void setPnml_netcontentelement(PNML_NetContentElement pnml_netcontentelement) {
        this.pnml_netcontentelement = pnml_netcontentelement;
    }
    public PNML_NodeGraphics getPnml_nodegraphics() {
        return pnml_nodegraphics;
    }

    public void setPnml_nodegraphics(PNML_NodeGraphics pnml_nodegraphics) {
        this.pnml_nodegraphics = pnml_nodegraphics;
    }

}