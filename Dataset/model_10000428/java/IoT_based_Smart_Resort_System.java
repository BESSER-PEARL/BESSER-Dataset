





import java.util.List;
import java.util.ArrayList;

public class IoT_based_Smart_Resort_System  {

    private boolean Status;
    private float Update;



    public IoT_based_Smart_Resort_System(
        boolean Status,        float Update    ) {
        this.Status = Status;
        this.Update = Update;
    }


    public boolean getStatus() {
        return Status;
    }

    public void setStatus(boolean Status) {
        this.Status = Status;
    }
    public float getUpdate() {
        return Update;
    }

    public void setUpdate(float Update) {
        this.Update = Update;
    }


}