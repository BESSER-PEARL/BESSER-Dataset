





import java.util.List;
import java.util.ArrayList;

public class timedAutomata_core_Location extends Position, core_TAElement {

    private String committed;
    private String urgent;



    public timedAutomata_core_Location(
        String committed,        String urgent    ) {
        super(
        );
        this.committed = committed;
        this.urgent = urgent;
    }


    public String getCommitted() {
        return committed;
    }

    public void setCommitted(String committed) {
        this.committed = committed;
    }
    public String getUrgent() {
        return urgent;
    }

    public void setUrgent(String urgent) {
        this.urgent = urgent;
    }


}