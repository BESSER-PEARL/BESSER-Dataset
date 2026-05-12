





import java.util.List;
import java.util.ArrayList;

public class Inventory  {

    private String Status;
    private String type;





    private Manager manager;


    public Inventory(
        String Status,        String type    ) {
        this.Status = Status;
        this.type = type;
    }


    public String getStatus() {
        return Status;
    }

    public void setStatus(String Status) {
        this.Status = Status;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public Manager getManager() {
        return manager;
    }

    public void setManager(Manager manager) {
        this.manager = manager;
    }

}