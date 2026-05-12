





import java.util.List;
import java.util.ArrayList;

public class Sensor  {

    private boolean detectingAnomaly;



    public Sensor(
        boolean detectingAnomaly    ) {
        this.detectingAnomaly = detectingAnomaly;
    }


    public boolean getDetectinganomaly() {
        return detectingAnomaly;
    }

    public void setDetectinganomaly(boolean detectingAnomaly) {
        this.detectingAnomaly = detectingAnomaly;
    }


}