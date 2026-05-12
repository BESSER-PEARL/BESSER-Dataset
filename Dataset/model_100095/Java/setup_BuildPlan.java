





import java.util.List;
import java.util.ArrayList;

public class setup_BuildPlan  {

    private String name;





    private setup_MylynBuildsTask setup_mylynbuildstask;


    public setup_BuildPlan(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public setup_MylynBuildsTask getSetup_mylynbuildstask() {
        return setup_mylynbuildstask;
    }

    public void setSetup_mylynbuildstask(setup_MylynBuildsTask setup_mylynbuildstask) {
        this.setup_mylynbuildstask = setup_mylynbuildstask;
    }

}