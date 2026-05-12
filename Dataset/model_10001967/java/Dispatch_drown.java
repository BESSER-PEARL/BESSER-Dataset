





import java.util.List;
import java.util.ArrayList;

public class Dispatch_drown  {

    private String Drown_ID;
    private String Camera_ID;



    public Dispatch_drown(
        String Drown_ID,        String Camera_ID    ) {
        this.Drown_ID = Drown_ID;
        this.Camera_ID = Camera_ID;
    }


    public String getDrown_id() {
        return Drown_ID;
    }

    public void setDrown_id(String Drown_ID) {
        this.Drown_ID = Drown_ID;
    }
    public String getCamera_id() {
        return Camera_ID;
    }

    public void setCamera_id(String Camera_ID) {
        this.Camera_ID = Camera_ID;
    }


}