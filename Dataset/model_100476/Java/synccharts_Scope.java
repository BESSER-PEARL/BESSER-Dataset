





import java.util.List;
import java.util.ArrayList;

public class synccharts_Scope extends Annotatable {

    private String id;
    private String label;
    private String interfaceDeclaration;





    private List<synccharts_Action> synccharts_actions;




    private synccharts_Action synccharts_action;




    private List<synccharts_Action> synccharts_actions;




    private List<synccharts_Action> synccharts_actions;


    public synccharts_Scope(
        String id,        String label,        String interfaceDeclaration    ) {
        super(
        );
        this.id = id;
        this.label = label;
        this.interfaceDeclaration = interfaceDeclaration;
        this.synccharts_actions = new ArrayList<>();
        this.synccharts_actions = new ArrayList<>();
        this.synccharts_actions = new ArrayList<>();
    }

    public synccharts_Scope(
        String id,        String label,        String interfaceDeclaration        ArrayList<synccharts_Action> synccharts_actions,        ArrayList<synccharts_Action> synccharts_actions,        ArrayList<synccharts_Action> synccharts_actions    ) {
        this.id = id;
        this.label = label;
        this.interfaceDeclaration = interfaceDeclaration;
        this.synccharts_actions = synccharts_actions;
        this.synccharts_actions = synccharts_actions;
        this.synccharts_actions = synccharts_actions;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getInterfacedeclaration() {
        return interfaceDeclaration;
    }

    public void setInterfacedeclaration(String interfaceDeclaration) {
        this.interfaceDeclaration = interfaceDeclaration;
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

}