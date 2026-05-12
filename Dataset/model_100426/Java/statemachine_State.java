





import java.util.List;
import java.util.ArrayList;

public class statemachine_State extends Node {

    private String do;
    private String entry;
    private String exit;





    private List<statemachine_Region> statemachine_regions;


    public statemachine_State(
        String do,        String entry,        String exit    ) {
        super(
        );
        this.do = do;
        this.entry = entry;
        this.exit = exit;
        this.statemachine_regions = new ArrayList<>();
    }

    public statemachine_State(
        String do,        String entry,        String exit        ArrayList<statemachine_Region> statemachine_regions    ) {
        this.do = do;
        this.entry = entry;
        this.exit = exit;
        this.statemachine_regions = statemachine_regions;
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

    public List<statemachine_Region> getStatemachine_regions() {
        return statemachine_regions;
    }

    public void addStatemachine_region(Statemachine_region statemachine_region) {
        this.statemachine_regions.add(statemachine_region);
    }

}