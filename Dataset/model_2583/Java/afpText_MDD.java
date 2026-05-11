





import java.util.List;
import java.util.ArrayList;

public class afpText_MDD extends structuredField {

    private String MDDFlgs;
    private String YmUnits;
    private String XmSize;
    private String XmBase;
    private String YmSize;
    private String XmUnits;
    private String YmBase;



    public afpText_MDD(
        String MDDFlgs,        String YmUnits,        String XmSize,        String XmBase,        String YmSize,        String XmUnits,        String YmBase    ) {
        super(
        );
        this.MDDFlgs = MDDFlgs;
        this.YmUnits = YmUnits;
        this.XmSize = XmSize;
        this.XmBase = XmBase;
        this.YmSize = YmSize;
        this.XmUnits = XmUnits;
        this.YmBase = YmBase;
    }


    public String getMddflgs() {
        return MDDFlgs;
    }

    public void setMddflgs(String MDDFlgs) {
        this.MDDFlgs = MDDFlgs;
    }
    public String getYmunits() {
        return YmUnits;
    }

    public void setYmunits(String YmUnits) {
        this.YmUnits = YmUnits;
    }
    public String getXmsize() {
        return XmSize;
    }

    public void setXmsize(String XmSize) {
        this.XmSize = XmSize;
    }
    public String getXmbase() {
        return XmBase;
    }

    public void setXmbase(String XmBase) {
        this.XmBase = XmBase;
    }
    public String getYmsize() {
        return YmSize;
    }

    public void setYmsize(String YmSize) {
        this.YmSize = YmSize;
    }
    public String getXmunits() {
        return XmUnits;
    }

    public void setXmunits(String XmUnits) {
        this.XmUnits = XmUnits;
    }
    public String getYmbase() {
        return YmBase;
    }

    public void setYmbase(String YmBase) {
        this.YmBase = YmBase;
    }


}