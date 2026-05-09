





import java.util.List;
import java.util.ArrayList;

public class statemachine_State extends Node {

    private String do;
    private String entry;
    private String exit;



    public statemachine_State(
        String do,        String entry,        String exit    ) {
        super(
        );
        this.do = do;
        this.entry = entry;
        this.exit = exit;
    }


    public String getDo() {
        return do;
    }

    public void setDo(String do) {
        this.do = do;
    }
    public String getEntry() {
        return entry;
    }

    public void setEntry(String entry) {
        this.entry = entry;
    }
    public String getExit() {
        return exit;
    }

    public void setExit(String exit) {
        this.exit = exit;
    }


}