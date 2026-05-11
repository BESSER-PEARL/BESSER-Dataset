





import java.util.List;
import java.util.ArrayList;

public class spinefm_RFModel_Rule  {

    private String id;





    private ConfigurationState configurationstate;




    private SystemActionModel_ActionOnFM systemactionmodel_actiononfm;


    public spinefm_RFModel_Rule(
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
    public SystemActionModel_ActionOnFM getSystemactionmodel_actiononfm() {
        return systemactionmodel_actiononfm;
    }

    public void setSystemactionmodel_actiononfm(SystemActionModel_ActionOnFM systemactionmodel_actiononfm) {
        this.systemactionmodel_actiononfm = systemactionmodel_actiononfm;
    }

}