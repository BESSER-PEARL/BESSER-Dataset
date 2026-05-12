





import java.util.List;
import java.util.ArrayList;

public class System  {

    private float Update;
    private boolean Status;



    public System(
        float Update,        boolean Status    ) {
        this.Update = Update;
        this.Status = Status;
    }


    public float getUpdate() {
        return Update;
    }

    public void setUpdate(float Update) {
        this.Update = Update;
    }
    public boolean getStatus() {
        return Status;
    }

    public void setStatus(boolean Status) {
        this.Status = Status;
    }


}