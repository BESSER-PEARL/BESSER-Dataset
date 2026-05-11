





import java.util.List;
import java.util.ArrayList;

public class afpText_MeasurementUnits extends triplet {

    private String XoaUnits;
    private String XoaBase;
    private String YoaBase;
    private String YoaUnits;



    public afpText_MeasurementUnits(
        String XoaUnits,        String XoaBase,        String YoaBase,        String YoaUnits    ) {
        super(
        );
        this.XoaUnits = XoaUnits;
        this.XoaBase = XoaBase;
        this.YoaBase = YoaBase;
        this.YoaUnits = YoaUnits;
    }


    public String getXoaunits() {
        return XoaUnits;
    }

    public void setXoaunits(String XoaUnits) {
        this.XoaUnits = XoaUnits;
    }
    public String getXoabase() {
        return XoaBase;
    }

    public void setXoabase(String XoaBase) {
        this.XoaBase = XoaBase;
    }
    public String getYoabase() {
        return YoaBase;
    }

    public void setYoabase(String YoaBase) {
        this.YoaBase = YoaBase;
    }
    public String getYoaunits() {
        return YoaUnits;
    }

    public void setYoaunits(String YoaUnits) {
        this.YoaUnits = YoaUnits;
    }


}