





import java.util.List;
import java.util.ArrayList;

public class spinefm_ProcessModel_ConfigurationProcessStep  {

    private boolean userConfig;
    private String description;
    private String id;





    private Configuration configuration;




    private DomainElement domainelement;


    public spinefm_ProcessModel_ConfigurationProcessStep(
        boolean userConfig,        String description,        String id    ) {
        this.userConfig = userConfig;
        this.description = description;
        this.id = id;
    }


    public boolean getUserconfig() {
        return userConfig;
    }

    public void setUserconfig(boolean userConfig) {
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

    public Configuration getConfiguration() {
        return configuration;
    }

    public void setConfiguration(Configuration configuration) {
        this.configuration = configuration;
    }
    public DomainElement getDomainelement() {
        return domainelement;
    }

    public void setDomainelement(DomainElement domainelement) {
        this.domainelement = domainelement;
    }

}