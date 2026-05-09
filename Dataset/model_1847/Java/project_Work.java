





import java.util.List;
import java.util.ArrayList;

public class project_Work extends TaskTimesheetAttribute, NewTaskAttribute {

    private float value;
    private String unit;



    public project_Work(
        float value,        String unit    ) {
        super(
        );
        this.value = value;
        this.unit = unit;
    }


    public float getValue() {
        return value;
    }

    public void setValue(float value) {
        this.value = value;
    }
    public String getUnit() {
        return unit;
    }

    public void setUnit(String unit) {
        this.unit = unit;
    }


}