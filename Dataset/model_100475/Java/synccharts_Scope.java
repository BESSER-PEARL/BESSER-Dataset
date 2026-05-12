





import java.util.List;
import java.util.ArrayList;

public class synccharts_Scope extends Annotatable {

    private String interfaceDeclaration;
    private String label;
    private String id;





    private List<synccharts_Variable> synccharts_variables;




    private List<synccharts_Action> synccharts_actions;




    private List<synccharts_Action> synccharts_actions;




    private List<synccharts_Action> synccharts_actions;




    private synccharts_Action synccharts_action;


    public synccharts_Scope(
        String interfaceDeclaration,        String label,        String id    ) {
        super(
        );
        this.interfaceDeclaration = interfaceDeclaration;
        this.label = label;
        this.id = id;
        this.synccharts_variables = new ArrayList<>();
        this.synccharts_actions = new ArrayList<>();
        this.synccharts_actions = new ArrayList<>();
        this.synccharts_actions = new ArrayList<>();
    }

    public synccharts_Scope(
        String interfaceDeclaration,        String label,        String id        ArrayList<synccharts_Variable> synccharts_variables,        ArrayList<synccharts_Action> synccharts_actions,        ArrayList<synccharts_Action> synccharts_actions,        ArrayList<synccharts_Action> synccharts_actions    ) {
        this.interfaceDeclaration = interfaceDeclaration;
        this.label = label;
        this.id = id;
        this.synccharts_variables = synccharts_variables;
        this.synccharts_actions = synccharts_actions;
        this.synccharts_actions = synccharts_actions;
        this.synccharts_actions = synccharts_actions;
    }

    public String getInterfacedeclaration() {
        return interfaceDeclaration;
    }

    public void setInterfacedeclaration(String interfaceDeclaration) {
        this.interfaceDeclaration = interfaceDeclaration;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public List<synccharts_Variable> getSynccharts_variables() {
        return synccharts_variables;
    }

    public void addSynccharts_variable(Synccharts_variable synccharts_variable) {
        this.synccharts_variables.add(synccharts_variable);
    }
    public List<synccharts_Action> getSynccharts_actions() {
        return synccharts_actions;
    }

    public void addSynccharts_action(Synccharts_action synccharts_action) {
        this.synccharts_actions.add(synccharts_action);
    }
    public List<synccharts_Action> getSynccharts_actions() {
        return synccharts_actions;
    }

    public void addSynccharts_action(Synccharts_action synccharts_action) {
        this.synccharts_actions.add(synccharts_action);
    }
    public List<synccharts_Action> getSynccharts_actions() {
        return synccharts_actions;
    }

    public void addSynccharts_action(Synccharts_action synccharts_action) {
        this.synccharts_actions.add(synccharts_action);
    }
    public synccharts_Action getSynccharts_action() {
        return synccharts_action;
    }

    public void setSynccharts_action(synccharts_Action synccharts_action) {
        this.synccharts_action = synccharts_action;
    }

}