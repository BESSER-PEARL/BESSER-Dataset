





import java.util.List;
import java.util.ArrayList;

public class NetContent  {






    private PNML_NetElement pnml_netelement;




    private PNML_Module pnml_module;




    private PNML_Page pnml_page;


    public NetContent(
    ) {
    }



    public PNML_NetElement getPnml_netelement() {
        return pnml_netelement;
    }

    public void setPnml_netelement(PNML_NetElement pnml_netelement) {
        this.pnml_netelement = pnml_netelement;
    }
    public PNML_Module getPnml_module() {
        return pnml_module;
    }

    public void setPnml_module(PNML_Module pnml_module) {
        this.pnml_module = pnml_module;
    }
    public PNML_Page getPnml_page() {
        return pnml_page;
    }

    public void setPnml_page(PNML_Page pnml_page) {
        this.pnml_page = pnml_page;
    }

}