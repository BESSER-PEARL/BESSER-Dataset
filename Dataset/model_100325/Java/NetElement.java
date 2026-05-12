





import java.util.List;
import java.util.ArrayList;

public class NetElement  {






    private PNML_NetContent pnml_netcontent;




    private PNML_PNMLDocument pnml_pnmldocument;


    public NetElement(
    ) {
    }



    public PNML_NetContent getPnml_netcontent() {
        return pnml_netcontent;
    }

    public void setPnml_netcontent(PNML_NetContent pnml_netcontent) {
        this.pnml_netcontent = pnml_netcontent;
    }
    public PNML_PNMLDocument getPnml_pnmldocument() {
        return pnml_pnmldocument;
    }

    public void setPnml_pnmldocument(PNML_PNMLDocument pnml_pnmldocument) {
        this.pnml_pnmldocument = pnml_pnmldocument;
    }

}