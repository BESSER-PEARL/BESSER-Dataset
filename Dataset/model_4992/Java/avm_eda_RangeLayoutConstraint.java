





import java.util.List;
import java.util.ArrayList;

public class avm_eda_RangeLayoutConstraint extends PcbLayoutConstraint {

    private String Type;
    private String XRangeMin;
    private String YRangeMin;
    private String YRangeMax;
    private String XRangeMax;
    private String LayerRange;



    public avm_eda_RangeLayoutConstraint(
        String Type,        String XRangeMin,        String YRangeMin,        String YRangeMax,        String XRangeMax,        String LayerRange    ) {
        super(
        );
        this.Type = Type;
        this.XRangeMin = XRangeMin;
        this.YRangeMin = YRangeMin;
        this.YRangeMax = YRangeMax;
        this.XRangeMax = XRangeMax;
        this.LayerRange = LayerRange;
    }


    public String getType() {
        return Type;
    }

    public void setType(String Type) {
        this.Type = Type;
    }
    public String getXrangemin() {
        return XRangeMin;
    }

    public void setXrangemin(String XRangeMin) {
        this.XRangeMin = XRangeMin;
    }
    public String getYrangemin() {
        return YRangeMin;
    }

    public void setYrangemin(String YRangeMin) {
        this.YRangeMin = YRangeMin;
    }
    public String getYrangemax() {
        return YRangeMax;
    }

    public void setYrangemax(String YRangeMax) {
        this.YRangeMax = YRangeMax;
    }
    public String getXrangemax() {
        return XRangeMax;
    }

    public void setXrangemax(String XRangeMax) {
        this.XRangeMax = XRangeMax;
    }
    public String getLayerrange() {
        return LayerRange;
    }

    public void setLayerrange(String LayerRange) {
        this.LayerRange = LayerRange;
    }


}