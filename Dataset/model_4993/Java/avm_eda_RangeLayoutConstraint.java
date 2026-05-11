





import java.util.List;
import java.util.ArrayList;

public class avm_eda_RangeLayoutConstraint extends PcbLayoutConstraint {

    private String LayerRange;
    private String YRangeMax;
    private String YRangeMin;
    private String XRangeMin;
    private String XRangeMax;
    private String Type;



    public avm_eda_RangeLayoutConstraint(
        String LayerRange,        String YRangeMax,        String YRangeMin,        String XRangeMin,        String XRangeMax,        String Type    ) {
        super(
        );
        this.LayerRange = LayerRange;
        this.YRangeMax = YRangeMax;
        this.YRangeMin = YRangeMin;
        this.XRangeMin = XRangeMin;
        this.XRangeMax = XRangeMax;
        this.Type = Type;
    }


    public String getLayerrange() {
        return LayerRange;
    }

    public void setLayerrange(String LayerRange) {
        this.LayerRange = LayerRange;
    }
    public String getYrangemax() {
        return YRangeMax;
    }

    public void setYrangemax(String YRangeMax) {
        this.YRangeMax = YRangeMax;
    }
    public String getYrangemin() {
        return YRangeMin;
    }

    public void setYrangemin(String YRangeMin) {
        this.YRangeMin = YRangeMin;
    }
    public String getXrangemin() {
        return XRangeMin;
    }

    public void setXrangemin(String XRangeMin) {
        this.XRangeMin = XRangeMin;
    }
    public String getXrangemax() {
        return XRangeMax;
    }

    public void setXrangemax(String XRangeMax) {
        this.XRangeMax = XRangeMax;
    }
    public String getType() {
        return Type;
    }

    public void setType(String Type) {
        this.Type = Type;
    }


}