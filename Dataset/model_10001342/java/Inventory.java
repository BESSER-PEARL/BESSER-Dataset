





import java.util.List;
import java.util.ArrayList;

public class Inventory  {

    private String Status;
    private String Type;



    public Inventory(
        String Status,        String Type    ) {
        this.Status = Status;
        this.Type = Type;
    }


    public String getStatus() {
        return Status;
    }

    public void setStatus(String Status) {
        this.Status = Status;
    }
    public String getType() {
        return Type;
    }

    public void setType(String Type) {
        this.Type = Type;
    }


}