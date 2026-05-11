





import java.util.List;
import java.util.ArrayList;

public class ir_PostProcessingInfo extends IrAnnotable {

    private float periodValue;



    public ir_PostProcessingInfo(
        float periodValue    ) {
        super(
        );
        this.periodValue = periodValue;
    }


    public float getPeriodvalue() {
        return periodValue;
    }

    public void setPeriodvalue(float periodValue) {
        this.periodValue = periodValue;
    }


}