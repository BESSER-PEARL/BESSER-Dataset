





import java.util.List;
import java.util.ArrayList;

public class traces_Value  {

    private float valueMin;
    private float valueMax;
    private float clockMin;
    private float clockMax;



    public traces_Value(
        float valueMin,        float valueMax,        float clockMin,        float clockMax    ) {
        this.valueMin = valueMin;
        this.valueMax = valueMax;
        this.clockMin = clockMin;
        this.clockMax = clockMax;
    }


    public float getValuemin() {
        return valueMin;
    }

    public void setValuemin(float valueMin) {
        this.valueMin = valueMin;
    }
    public float getValuemax() {
        return valueMax;
    }

    public void setValuemax(float valueMax) {
        this.valueMax = valueMax;
    }
    public float getClockmin() {
        return clockMin;
    }

    public void setClockmin(float clockMin) {
        this.clockMin = clockMin;
    }
    public float getClockmax() {
        return clockMax;
    }

    public void setClockmax(float clockMax) {
        this.clockMax = clockMax;
    }


}