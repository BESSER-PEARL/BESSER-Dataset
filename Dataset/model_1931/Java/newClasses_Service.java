





import java.util.List;
import java.util.ArrayList;

public class newClasses_Service extends ServiceType {

    private String status;
    private String id;





    private newClasses_ServiceHandler newclasses_servicehandler;


    public newClasses_Service(
        String status,        String id    ) {
        super(
        );
        this.status = status;
        this.id = id;
    }


    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public newClasses_ServiceHandler getNewclasses_servicehandler() {
        return newclasses_servicehandler;
    }

    public void setNewclasses_servicehandler(newClasses_ServiceHandler newclasses_servicehandler) {
        this.newclasses_servicehandler = newclasses_servicehandler;
    }

}