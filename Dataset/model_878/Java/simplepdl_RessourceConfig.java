





import java.util.List;
import java.util.ArrayList;

public class simplepdl_RessourceConfig extends ProcessElement {

    private String name;





    private simplepdl_RessourceInstance simplepdl_ressourceinstance;




    private List<simplepdl_RessourceInstance> simplepdl_ressourceinstances;




    private simplepdl_WorkDefinition simplepdl_workdefinition;




    private simplepdl_WorkDefinition simplepdl_workdefinition;


    public simplepdl_RessourceConfig(
        String name    ) {
        super(
        );
        this.name = name;
        this.simplepdl_ressourceinstances = new ArrayList<>();
    }

    public simplepdl_RessourceConfig(
        String name        ArrayList<simplepdl_RessourceInstance> simplepdl_ressourceinstances    ) {
        this.name = name;
        this.simplepdl_ressourceinstances = simplepdl_ressourceinstances;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public simplepdl_RessourceInstance getSimplepdl_ressourceinstance() {
        return simplepdl_ressourceinstance;
    }

    public void setSimplepdl_ressourceinstance(simplepdl_RessourceInstance simplepdl_ressourceinstance) {
        this.simplepdl_ressourceinstance = simplepdl_ressourceinstance;
    }
    public List<simplepdl_RessourceInstance> getSimplepdl_ressourceinstances() {
        return simplepdl_ressourceinstances;
    }

    public void addSimplepdl_ressourceinstance(Simplepdl_ressourceinstance simplepdl_ressourceinstance) {
        this.simplepdl_ressourceinstances.add(simplepdl_ressourceinstance);
    }
    public simplepdl_WorkDefinition getSimplepdl_workdefinition() {
        return simplepdl_workdefinition;
    }

    public void setSimplepdl_workdefinition(simplepdl_WorkDefinition simplepdl_workdefinition) {
        this.simplepdl_workdefinition = simplepdl_workdefinition;
    }
    public simplepdl_WorkDefinition getSimplepdl_workdefinition() {
        return simplepdl_workdefinition;
    }

    public void setSimplepdl_workdefinition(simplepdl_WorkDefinition simplepdl_workdefinition) {
        this.simplepdl_workdefinition = simplepdl_workdefinition;
    }

}