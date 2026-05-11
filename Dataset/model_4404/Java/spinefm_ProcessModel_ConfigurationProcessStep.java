





import java.util.List;
import java.util.ArrayList;

public class spinefm_ProcessModel_ConfigurationProcessStep  {

    private String description;
    private String id;
    private boolean userConfig;





    private List<Action> actions;




    private List<Action> actions;




    private DomainElement domainelement;




    private Configuration configuration;


    public spinefm_ProcessModel_ConfigurationProcessStep(
        String description,        String id,        boolean userConfig    ) {
        this.description = description;
        this.id = id;
        this.userConfig = userConfig;
        this.actions = new ArrayList<>();
        this.actions = new ArrayList<>();
    }

    public spinefm_ProcessModel_ConfigurationProcessStep(
        String description,        String id,        boolean userConfig        ArrayList<Action> actions,        ArrayList<Action> actions    ) {
        this.description = description;
        this.id = id;
        this.userConfig = userConfig;
        this.actions = actions;
        this.actions = actions;
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
    public boolean getUserconfig() {
        return userConfig;
    }

    public void setUserconfig(boolean userConfig) {
        this.userConfig = userConfig;
    }

    public List<Action> getActions() {
        return actions;
    }

    public void addAction(Action action) {
        this.actions.add(action);
    }
    public List<Action> getActions() {
        return actions;
    }

    public void addAction(Action action) {
        this.actions.add(action);
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

}