





import java.util.List;
import java.util.ArrayList;

public class actions_ActionResult  {

    private int version;
    private int id;



    public actions_ActionResult(
        int version,        int id    ) {
        this.version = version;
        this.id = id;
    }


    public int getVersion() {
        return version;
    }

    public void setVersion(int version) {
        this.version = version;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }


}