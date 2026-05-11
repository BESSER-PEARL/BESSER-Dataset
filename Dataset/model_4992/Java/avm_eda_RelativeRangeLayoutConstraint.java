





import java.util.List;
import java.util.ArrayList;

public class avm_eda_RelativeRangeLayoutConstraint extends PcbLayoutConstraint {

    private String XRelativeRangeMin;
    private String RelativeLayer;
    private String YRelativeRangeMin;
    private String YRelativeRangeMax;
    private String XRelativeRangeMax;



    public avm_eda_RelativeRangeLayoutConstraint(
        String XRelativeRangeMin,        String RelativeLayer,        String YRelativeRangeMin,        String YRelativeRangeMax,        String XRelativeRangeMax    ) {
        super(
        );
        this.XRelativeRangeMin = XRelativeRangeMin;
        this.RelativeLayer = RelativeLayer;
        this.YRelativeRangeMin = YRelativeRangeMin;
        this.YRelativeRangeMax = YRelativeRangeMax;
        this.XRelativeRangeMax = XRelativeRangeMax;
    }


    public String getXrelativerangemin() {
        return XRelativeRangeMin;
    }

    public void setXrelativerangemin(String XRelativeRangeMin) {
        this.XRelativeRangeMin = XRelativeRangeMin;
    }
    public String getRelativelayer() {
        return RelativeLayer;
    }

    public void setRelativelayer(String RelativeLayer) {
        this.RelativeLayer = RelativeLayer;
    }
    public String getYrelativerangemin() {
        return YRelativeRangeMin;
    }

    public void setYrelativerangemin(String YRelativeRangeMin) {
        this.YRelativeRangeMin = YRelativeRangeMin;
    }
    public String getYrelativerangemax() {
        return YRelativeRangeMax;
    }

    public void setYrelativerangemax(String YRelativeRangeMax) {
        this.YRelativeRangeMax = YRelativeRangeMax;
    }
    public String getXrelativerangemax() {
        return XRelativeRangeMax;
    }

    public void setXrelativerangemax(String XRelativeRangeMax) {
        this.XRelativeRangeMax = XRelativeRangeMax;
    }


}