





import java.util.List;
import java.util.ArrayList;

public class afpText_CDD extends structuredField {

    private String XocBase;
    private String YocUnits;
    private String XocUnits;
    private String YocSize;
    private String XocSize;
    private String YocBase;



    public afpText_CDD(
        String XocBase,        String YocUnits,        String XocUnits,        String YocSize,        String XocSize,        String YocBase    ) {
        super(
        );
        this.XocBase = XocBase;
        this.YocUnits = YocUnits;
        this.XocUnits = XocUnits;
        this.YocSize = YocSize;
        this.XocSize = XocSize;
        this.YocBase = YocBase;
    }


    public String getXocbase() {
        return XocBase;
    }

    public void setXocbase(String XocBase) {
        this.XocBase = XocBase;
    }
    public String getYocunits() {
        return YocUnits;
    }

    public void setYocunits(String YocUnits) {
        this.YocUnits = YocUnits;
    }
    public String getXocunits() {
        return XocUnits;
    }

    public void setXocunits(String XocUnits) {
        this.XocUnits = XocUnits;
    }
    public String getYocsize() {
        return YocSize;
    }

    public void setYocsize(String YocSize) {
        this.YocSize = YocSize;
    }
    public String getXocsize() {
        return XocSize;
    }

    public void setXocsize(String XocSize) {
        this.XocSize = XocSize;
    }
    public String getYocbase() {
        return YocBase;
    }

    public void setYocbase(String YocBase) {
        this.YocBase = YocBase;
    }


}