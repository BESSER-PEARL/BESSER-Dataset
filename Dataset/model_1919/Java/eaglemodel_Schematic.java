





import java.util.List;
import java.util.ArrayList;

public class eaglemodel_Schematic  {

    private String xrefpart;
    private String xreflabel;



    public eaglemodel_Schematic(
        String xrefpart,        String xreflabel    ) {
        this.xrefpart = xrefpart;
        this.xreflabel = xreflabel;
    }


    public String getXrefpart() {
        return xrefpart;
    }

    public void setXrefpart(String xrefpart) {
        this.xrefpart = xrefpart;
    }
    public String getXreflabel() {
        return xreflabel;
    }

    public void setXreflabel(String xreflabel) {
        this.xreflabel = xreflabel;
    }


}