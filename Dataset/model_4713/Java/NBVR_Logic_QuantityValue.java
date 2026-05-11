





import java.util.List;
import java.util.ArrayList;

public class NBVR_Logic_QuantityValue extends Constant {

    private String factor;
    private String unit;



    public NBVR_Logic_QuantityValue(
        String factor,        String unit    ) {
        super(
        );
        this.factor = factor;
        this.unit = unit;
    }


    public String getFactor() {
        return factor;
    }

    public void setFactor(String factor) {
        this.factor = factor;
    }
    public String getUnit() {
        return unit;
    }

    public void setUnit(String unit) {
        this.unit = unit;
    }


}