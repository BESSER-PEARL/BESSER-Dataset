





import java.util.List;
import java.util.ArrayList;

public class core_actionstep_ActionStep extends ProductIdentifiable, ThreadSensitive, PlatformDisposition {

    private boolean active;
    private String name;
    private boolean paused;



    public core_actionstep_ActionStep(
        boolean active,        String name,        boolean paused    ) {
        super(
        );
        this.active = active;
        this.name = name;
        this.paused = paused;
    }


    public boolean getActive() {
        return active;
    }

    public void setActive(boolean active) {
        this.active = active;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getPaused() {
        return paused;
    }

    public void setPaused(boolean paused) {
        this.paused = paused;
    }


}