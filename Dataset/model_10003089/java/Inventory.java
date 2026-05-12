





import java.util.List;
import java.util.ArrayList;

public class Inventory  {

    private String Type;
    private String Status;



    public Inventory(
        String Type,        String Status    ) {
        this.Type = Type;
        this.Status = Status;
    }


    public String getType() {
        return Type;
    }

    public void setType(String Type) {
        this.Type = Type;
    }
    public String getStatus() {
        return Status;
    }

    public void setStatus(String Status) {
        this.Status = Status;
    }


}