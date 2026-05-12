





import java.util.List;
import java.util.ArrayList;

public class PNMLDocument  {






    private PNML_Module pnml_module;




    private PNML_NetElement pnml_netelement;


    public PNMLDocument(
    ) {
    }



    public PNML_Module getPnml_module() {
        return pnml_module;
    }

    public void setPnml_module(PNML_Module pnml_module) {
        this.pnml_module = pnml_module;
    }
    public PNML_NetElement getPnml_netelement() {
        return pnml_netelement;
    }

    public void setPnml_netelement(PNML_NetElement pnml_netelement) {
        this.pnml_netelement = pnml_netelement;
    }

}