





import java.util.List;
import java.util.ArrayList;

public class dsl_timeUnitValue  {

    private String unit;





    private dsl_Task dsl_task;


    public dsl_timeUnitValue(
        String unit    ) {
        this.unit = unit;
    }


    public String getUnit() {
        return unit;
    }

    public void setUnit(String unit) {
        this.unit = unit;
    }

    public dsl_Task getDsl_task() {
        return dsl_task;
    }

    public void setDsl_task(dsl_Task dsl_task) {
        this.dsl_task = dsl_task;
    }

}