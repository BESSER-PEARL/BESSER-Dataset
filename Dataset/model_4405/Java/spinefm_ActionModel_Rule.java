





import java.util.List;
import java.util.ArrayList;

public class spinefm_ActionModel_Rule  {

    private String id;





    private ConfigurationState configurationstate;




    private Action action;


    public spinefm_ActionModel_Rule(
        String id    ) {
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public ConfigurationState getConfigurationstate() {
        return configurationstate;
    }

    public void setConfigurationstate(ConfigurationState configurationstate) {
        this.configurationstate = configurationstate;
    }
    public Action getAction() {
        return action;
    }

    public void setAction(Action action) {
        this.action = action;
    }

}