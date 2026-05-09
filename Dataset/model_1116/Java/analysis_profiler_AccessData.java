





import java.util.List;
import java.util.ArrayList;

public class analysis_profiler_AccessData  {

    private float min;
    private float average;
    private float accesses;
    private float total;
    private float max;



    public analysis_profiler_AccessData(
        float min,        float average,        float accesses,        float total,        float max    ) {
        this.min = min;
        this.average = average;
        this.accesses = accesses;
        this.total = total;
        this.max = max;
    }


    public float getMin() {
        return min;
    }

    public void setMin(float min) {
        this.min = min;
    }
    public float getAverage() {
        return average;
    }

    public void setAverage(float average) {
        this.average = average;
    }
    public float getAccesses() {
        return accesses;
    }

    public void setAccesses(float accesses) {
        this.accesses = accesses;
    }
    public float getTotal() {
        return total;
    }

    public void setTotal(float total) {
        this.total = total;
    }
    public float getMax() {
        return max;
    }

    public void setMax(float max) {
        this.max = max;
    }


}