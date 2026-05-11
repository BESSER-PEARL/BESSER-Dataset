





import java.util.List;
import java.util.ArrayList;

public class stateChart_State extends Vertex {

    private String exit;
    private String entry;
    private String action;



    public stateChart_State(
        String exit,        String entry,        String action    ) {
        super(
        );
        this.exit = exit;
        this.entry = entry;
        this.action = action;
    }


    public String getExit() {
        return exit;
    }

    public void setExit(String exit) {
        this.exit = exit;
    }
    public String getEntry() {
        return entry;
    }

    public void setEntry(String entry) {
        this.entry = entry;
    }
    public String getAction() {
        return action;
    }

    public void setAction(String action) {
        this.action = action;
    }


}