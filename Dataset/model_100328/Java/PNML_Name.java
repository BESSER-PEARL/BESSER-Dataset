





import java.util.List;
import java.util.ArrayList;

public class PNML_Name extends LabeledElement {






    private NetContent netcontent;




    private NetElement netelement;


    public PNML_Name(
    ) {
        super(
        );
    }



    public NetContent getNetcontent() {
        return netcontent;
    }

    public void setNetcontent(NetContent netcontent) {
        this.netcontent = netcontent;
    }
    public NetElement getNetelement() {
        return netelement;
    }

    public void setNetelement(NetElement netelement) {
        this.netelement = netelement;
    }

}