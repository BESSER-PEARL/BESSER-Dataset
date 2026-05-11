





import java.util.List;
import java.util.ArrayList;

public class avm_eda_RelativeRangeLayoutConstraint extends PcbLayoutConstraint {

    private String YRelativeRangeMin;
    private String RelativeLayer;
    private String YRelativeRangeMax;
    private String XRelativeRangeMin;
    private String XRelativeRangeMax;



    public avm_eda_RelativeRangeLayoutConstraint(
        String YRelativeRangeMin,        String RelativeLayer,        String YRelativeRangeMax,        String XRelativeRangeMin,        String XRelativeRangeMax    ) {
        super(
        );
        this.YRelativeRangeMin = YRelativeRangeMin;
        this.RelativeLayer = RelativeLayer;
        this.YRelativeRangeMax = YRelativeRangeMax;
        this.XRelativeRangeMin = XRelativeRangeMin;
        this.XRelativeRangeMax = XRelativeRangeMax;
    }


    public String getYrelativerangemin() {
        return YRelativeRangeMin;
    }

    public void setYrelativerangemin(String YRelativeRangeMin) {
        this.YRelativeRangeMin = YRelativeRangeMin;
    }
    public String getRelativelayer() {
        return RelativeLayer;
    }

    public void setRelativelayer(String RelativeLayer) {
        this.RelativeLayer = RelativeLayer;
    }
    public String getYrelativerangemax() {
        return YRelativeRangeMax;
    }

    public void setYrelativerangemax(String YRelativeRangeMax) {
        this.YRelativeRangeMax = YRelativeRangeMax;
    }
    public String getXrelativerangemin() {
        return XRelativeRangeMin;
    }

    public void setXrelativerangemin(String XRelativeRangeMin) {
        this.XRelativeRangeMin = XRelativeRangeMin;
    }
    public String getXrelativerangemax() {
        return XRelativeRangeMax;
    }

    public void setXrelativerangemax(String XRelativeRangeMax) {
        this.XRelativeRangeMax = XRelativeRangeMax;
    }


}