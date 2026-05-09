





import java.util.List;
import java.util.ArrayList;

public class MARTE_Library_TimeLibrary_TimedValueType  {

    private String value;
    private String expr;
    private String unit;
    private String onClock;



    public MARTE_Library_TimeLibrary_TimedValueType(
        String value,        String expr,        String unit,        String onClock    ) {
        this.value = value;
        this.expr = expr;
        this.unit = unit;
        this.onClock = onClock;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getExpr() {
        return expr;
    }

    public void setExpr(String expr) {
        this.expr = expr;
    }
    public String getUnit() {
        return unit;
    }

    public void setUnit(String unit) {
        this.unit = unit;
    }
    public String getOnclock() {
        return onClock;
    }

    public void setOnclock(String onClock) {
        this.onClock = onClock;
    }


}