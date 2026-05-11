





import java.util.List;
import java.util.ArrayList;

public class dsl_ColorSensor extends SensorType {

    private boolean distinct;



    public dsl_ColorSensor(
        boolean distinct    ) {
        super(
        );
        this.distinct = distinct;
    }


    public boolean getDistinct() {
        return distinct;
    }

    public void setDistinct(boolean distinct) {
        this.distinct = distinct;
    }


}