





import java.util.List;
import java.util.ArrayList;

public class spinefm_ProcessModel_ConfigurationProcessStep  {

    private String description;
    private String id;
    private String history;
    private String status;
    private boolean userConfig;





    private DomainElement domainelement;




    private Configuration configuration;




    private ConfigurationState configurationstate;




    private Context context;


    public spinefm_ProcessModel_ConfigurationProcessStep(
        String description,        String id,        String history,        String status,        boolean userConfig    ) {
        this.description = description;
        this.id = id;
        this.history = history;
        this.status = status;
        this.userConfig = userConfig;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getHistory() {
        return history;
    }

    public void setHistory(String history) {
        this.history = history;
    }
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public boolean getUserconfig() {
        return userConfig;
    }

    public void setUserconfig(boolean userConfig) {
        this.userConfig = userConfig;
    }

    public DomainElement getDomainelement() {
        return domainelement;
    }

    public void setDomainelement(DomainElement domainelement) {
        this.domainelement = domainelement;
    }
    public Configuration getConfiguration() {
        return configuration;
    }

    public void setConfiguration(Configuration configuration) {
        this.configuration = configuration;
    }
    public ConfigurationState getConfigurationstate() {
        return configurationstate;
    }

    public void setConfigurationstate(ConfigurationState configurationstate) {
        this.configurationstate = configurationstate;
    }
    public Context getContext() {
        return context;
    }

    public void setContext(Context context) {
        this.context = context;
    }

}