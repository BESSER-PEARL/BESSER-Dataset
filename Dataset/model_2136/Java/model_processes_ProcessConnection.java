





import java.util.List;
import java.util.ArrayList;

public class model_processes_ProcessConnection extends IModelConnection {

    private float labelY;
    private float labelX;
    private String condition;



    public model_processes_ProcessConnection(
        float labelY,        float labelX,        String condition    ) {
        super(
        );
        this.labelY = labelY;
        this.labelX = labelX;
        this.condition = condition;
    }


    public float getLabely() {
        return labelY;
    }

    public void setLabely(float labelY) {
        this.labelY = labelY;
    }
    public float getLabelx() {
        return labelX;
    }

    public void setLabelx(float labelX) {
        this.labelX = labelX;
    }
    public String getCondition() {
        return condition;
    }

    public void setCondition(String condition) {
        this.condition = condition;
    }


}