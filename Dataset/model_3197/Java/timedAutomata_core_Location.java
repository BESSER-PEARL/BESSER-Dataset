





import java.util.List;
import java.util.ArrayList;

public class timedAutomata_core_Location extends core_TAElement, Position {

    private String urgent;
    private String committed;



    public timedAutomata_core_Location(
        String urgent,        String committed    ) {
        super(
        );
        this.urgent = urgent;
        this.committed = committed;
    }


    public String getUrgent() {
        return urgent;
    }

    public void setUrgent(String urgent) {
        this.urgent = urgent;
    }
    public String getCommitted() {
        return committed;
    }

    public void setCommitted(String committed) {
        this.committed = committed;
    }


}