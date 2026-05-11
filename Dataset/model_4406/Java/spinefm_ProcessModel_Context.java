





import java.util.List;
import java.util.ArrayList;

public class spinefm_ProcessModel_Context  {

    private String id;





    private List<ConfigurationProcessStep> configurationprocesssteps;


    public spinefm_ProcessModel_Context(
        String id    ) {
        this.id = id;
        this.configurationprocesssteps = new ArrayList<>();
    }

    public spinefm_ProcessModel_Context(
        String id        ArrayList<ConfigurationProcessStep> configurationprocesssteps    ) {
        this.id = id;
        this.configurationprocesssteps = configurationprocesssteps;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public List<ConfigurationProcessStep> getConfigurationprocesssteps() {
        return configurationprocesssteps;
    }

    public void addConfigurationprocessstep(Configurationprocessstep configurationprocessstep) {
        this.configurationprocesssteps.add(configurationprocessstep);
    }

}