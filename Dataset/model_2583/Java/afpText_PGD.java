





import java.util.List;
import java.util.ArrayList;

public class afpText_PGD extends structuredField {

    private String XpgSize;
    private String Reserved;
    private String XpgBase;
    private String YpgUnits;
    private String XpgUnits;
    private String YpgBase;
    private String YpgSize;



    public afpText_PGD(
        String XpgSize,        String Reserved,        String XpgBase,        String YpgUnits,        String XpgUnits,        String YpgBase,        String YpgSize    ) {
        super(
        );
        this.XpgSize = XpgSize;
        this.Reserved = Reserved;
        this.XpgBase = XpgBase;
        this.YpgUnits = YpgUnits;
        this.XpgUnits = XpgUnits;
        this.YpgBase = YpgBase;
        this.YpgSize = YpgSize;
    }


    public String getXpgsize() {
        return XpgSize;
    }

    public void setXpgsize(String XpgSize) {
        this.XpgSize = XpgSize;
    }
    public String getReserved() {
        return Reserved;
    }

    public void setReserved(String Reserved) {
        this.Reserved = Reserved;
    }
    public String getXpgbase() {
        return XpgBase;
    }

    public void setXpgbase(String XpgBase) {
        this.XpgBase = XpgBase;
    }
    public String getYpgunits() {
        return YpgUnits;
    }

    public void setYpgunits(String YpgUnits) {
        this.YpgUnits = YpgUnits;
    }
    public String getXpgunits() {
        return XpgUnits;
    }

    public void setXpgunits(String XpgUnits) {
        this.XpgUnits = XpgUnits;
    }
    public String getYpgbase() {
        return YpgBase;
    }

    public void setYpgbase(String YpgBase) {
        this.YpgBase = YpgBase;
    }
    public String getYpgsize() {
        return YpgSize;
    }

    public void setYpgsize(String YpgSize) {
        this.YpgSize = YpgSize;
    }


}