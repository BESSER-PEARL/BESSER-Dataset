





import java.util.List;
import java.util.ArrayList;

public class Inventory  {

    private String type;
    private String status;





    private Manager manager;


    public Inventory(
        String type,        String status    ) {
        this.type = type;
        this.status = status;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public Manager getManager() {
        return manager;
    }

    public void setManager(Manager manager) {
        this.manager = manager;
    }

}