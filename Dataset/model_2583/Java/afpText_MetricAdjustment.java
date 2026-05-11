





import java.util.List;
import java.util.ArrayList;

public class afpText_MetricAdjustment extends triplet {

    private String VUniformIncrement;
    private String HBaselineIncrement;
    private String VBaselineIncrement;
    private String YUPUB;
    private String XUPUB;
    private String UnitBase;
    private String HUniformIncrement;



    public afpText_MetricAdjustment(
        String VUniformIncrement,        String HBaselineIncrement,        String VBaselineIncrement,        String YUPUB,        String XUPUB,        String UnitBase,        String HUniformIncrement    ) {
        super(
        );
        this.VUniformIncrement = VUniformIncrement;
        this.HBaselineIncrement = HBaselineIncrement;
        this.VBaselineIncrement = VBaselineIncrement;
        this.YUPUB = YUPUB;
        this.XUPUB = XUPUB;
        this.UnitBase = UnitBase;
        this.HUniformIncrement = HUniformIncrement;
    }


    public String getVuniformincrement() {
        return VUniformIncrement;
    }

    public void setVuniformincrement(String VUniformIncrement) {
        this.VUniformIncrement = VUniformIncrement;
    }
    public String getHbaselineincrement() {
        return HBaselineIncrement;
    }

    public void setHbaselineincrement(String HBaselineIncrement) {
        this.HBaselineIncrement = HBaselineIncrement;
    }
    public String getVbaselineincrement() {
        return VBaselineIncrement;
    }

    public void setVbaselineincrement(String VBaselineIncrement) {
        this.VBaselineIncrement = VBaselineIncrement;
    }
    public String getYupub() {
        return YUPUB;
    }

    public void setYupub(String YUPUB) {
        this.YUPUB = YUPUB;
    }
    public String getXupub() {
        return XUPUB;
    }

    public void setXupub(String XUPUB) {
        this.XUPUB = XUPUB;
    }
    public String getUnitbase() {
        return UnitBase;
    }

    public void setUnitbase(String UnitBase) {
        this.UnitBase = UnitBase;
    }
    public String getHuniformincrement() {
        return HUniformIncrement;
    }

    public void setHuniformincrement(String HUniformIncrement) {
        this.HUniformIncrement = HUniformIncrement;
    }


}