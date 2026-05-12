





import java.util.List;
import java.util.ArrayList;

public class Notification  {

    private float TempThreshold;
    private float SmokeThreshold;



    public Notification(
        float TempThreshold,        float SmokeThreshold    ) {
        this.TempThreshold = TempThreshold;
        this.SmokeThreshold = SmokeThreshold;
    }


    public float getTempthreshold() {
        return TempThreshold;
    }

    public void setTempthreshold(float TempThreshold) {
        this.TempThreshold = TempThreshold;
    }
    public float getSmokethreshold() {
        return SmokeThreshold;
    }

    public void setSmokethreshold(float SmokeThreshold) {
        this.SmokeThreshold = SmokeThreshold;
    }


}