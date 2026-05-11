





import java.util.List;
import java.util.ArrayList;

public class FlowDesigner_NamedState extends Target, Source {

    private String entry;
    private String activity;
    private String exit;
    private String name;



    public FlowDesigner_NamedState(
        String entry,        String activity,        String exit,        String name    ) {
        super(
        );
        this.entry = entry;
        this.activity = activity;
        this.exit = exit;
        this.name = name;
    }


    public String getEntry() {
        return entry;
    }

    public void setEntry(String entry) {
        this.entry = entry;
    }
    public String getActivity() {
        return activity;
    }

    public void setActivity(String activity) {
        this.activity = activity;
    }
    public String getExit() {
        return exit;
    }

    public void setExit(String exit) {
        this.exit = exit;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}