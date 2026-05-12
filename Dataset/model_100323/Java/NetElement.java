





import java.util.List;
import java.util.ArrayList;

public class NetElement  {






    private PNML_PNMLDocument pnml_pnmldocument;




    private PNML_NetGraphics pnml_netgraphics;




    private PNML_NetContent pnml_netcontent;


    public NetElement(
    ) {
    }



    public PNML_PNMLDocument getPnml_pnmldocument() {
        return pnml_pnmldocument;
    }

    public void setPnml_pnmldocument(PNML_PNMLDocument pnml_pnmldocument) {
        this.pnml_pnmldocument = pnml_pnmldocument;
    }
    public PNML_NetGraphics getPnml_netgraphics() {
        return pnml_netgraphics;
    }

    public void setPnml_netgraphics(PNML_NetGraphics pnml_netgraphics) {
        this.pnml_netgraphics = pnml_netgraphics;
    }
    public PNML_NetContent getPnml_netcontent() {
        return pnml_netcontent;
    }

    public void setPnml_netcontent(PNML_NetContent pnml_netcontent) {
        this.pnml_netcontent = pnml_netcontent;
    }

}