





import java.util.List;
import java.util.ArrayList;

public class setup_SetupTask  {

    private boolean disabled;
    private String documentation;
    private String excludedTriggers;
    private String scope;





    private List<setup_SetupTask> setup_setuptasks;




    private List<setup_ConfigurableItem> setup_configurableitems;


    public setup_SetupTask(
        boolean disabled,        String documentation,        String excludedTriggers,        String scope    ) {
        this.disabled = disabled;
        this.documentation = documentation;
        this.excludedTriggers = excludedTriggers;
        this.scope = scope;
        this.setup_setuptasks = new ArrayList<>();
        this.setup_configurableitems = new ArrayList<>();
    }

    public setup_SetupTask(
        boolean disabled,        String documentation,        String excludedTriggers,        String scope        ArrayList<setup_SetupTask> setup_setuptasks,        ArrayList<setup_ConfigurableItem> setup_configurableitems    ) {
        this.disabled = disabled;
        this.documentation = documentation;
        this.excludedTriggers = excludedTriggers;
        this.scope = scope;
        this.setup_setuptasks = setup_setuptasks;
        this.setup_configurableitems = setup_configurableitems;
    }

    public boolean getDisabled() {
        return disabled;
    }

    public void setDisabled(boolean disabled) {
        this.disabled = disabled;
    }
    public String getDocumentation() {
        return documentation;
    }

    public void setDocumentation(String documentation) {
        this.documentation = documentation;
    }
    public String getExcludedtriggers() {
        return excludedTriggers;
    }

    public void setExcludedtriggers(String excludedTriggers) {
        this.excludedTriggers = excludedTriggers;
    }
    public String getScope() {
        return scope;
    }

    public void setScope(String scope) {
        this.scope = scope;
    }

    public List<setup_SetupTask> getSetup_setuptasks() {
        return setup_setuptasks;
    }

    public void addSetup_setuptask(Setup_setuptask setup_setuptask) {
        this.setup_setuptasks.add(setup_setuptask);
    }
    public List<setup_ConfigurableItem> getSetup_configurableitems() {
        return setup_configurableitems;
    }

    public void addSetup_configurableitem(Setup_configurableitem setup_configurableitem) {
        this.setup_configurableitems.add(setup_configurableitem);
    }

}