





import java.util.List;
import java.util.ArrayList;

public class pimm_Actor extends ExecutableActor {

    private boolean configurationActor;
    private String memoryScriptPath;





    private pimm_Refinement pimm_refinement;


    public pimm_Actor(
        boolean configurationActor,        String memoryScriptPath    ) {
        super(
        );
        this.configurationActor = configurationActor;
        this.memoryScriptPath = memoryScriptPath;
    }


    public boolean getConfigurationactor() {
        return configurationActor;
    }

    public void setConfigurationactor(boolean configurationActor) {
        this.configurationActor = configurationActor;
    }
    public String getMemoryscriptpath() {
        return memoryScriptPath;
    }

    public void setMemoryscriptpath(String memoryScriptPath) {
        this.memoryScriptPath = memoryScriptPath;
    }

    public pimm_Refinement getPimm_refinement() {
        return pimm_refinement;
    }

    public void setPimm_refinement(pimm_Refinement pimm_refinement) {
        this.pimm_refinement = pimm_refinement;
    }

}