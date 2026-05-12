





import java.util.List;
import java.util.ArrayList;

public class Microcontroller  {

    private String Status;
    private float Update;



    public Microcontroller(
        String Status,        float Update    ) {
        this.Status = Status;
        this.Update = Update;
    }


    public String getStatus() {
        return Status;
    }

    public void setStatus(String Status) {
        this.Status = Status;
    }
    public float getUpdate() {
        return Update;
    }

    public void setUpdate(float Update) {
        this.Update = Update;
    }


}