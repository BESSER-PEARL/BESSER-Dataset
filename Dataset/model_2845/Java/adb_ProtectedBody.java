





import java.util.List;
import java.util.ArrayList;

public class adb_ProtectedBody extends ProperBody {

    private String idTask;
    private String identifier;



    public adb_ProtectedBody(
        String idTask,        String identifier    ) {
        super(
        );
        this.idTask = idTask;
        this.identifier = identifier;
    }


    public String getIdtask() {
        return idTask;
    }

    public void setIdtask(String idTask) {
        this.idTask = idTask;
    }
    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
    }


}