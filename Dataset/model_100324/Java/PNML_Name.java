





import java.util.List;
import java.util.ArrayList;

public class PNML_Name extends LabeledElement {






    private NetElement netelement;




    private NetContent netcontent;


    public PNML_Name(
    ) {
        super(
        );
    }



    public NetElement getNetelement() {
        return netelement;
    }

    public void setNetelement(NetElement netelement) {
        this.netelement = netelement;
    }
    public NetContent getNetcontent() {
        return netcontent;
    }

    public void setNetcontent(NetContent netcontent) {
        this.netcontent = netcontent;
    }

}