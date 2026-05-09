





import java.util.List;
import java.util.ArrayList;

public class simplepdl_RessourceSequence extends ProcessElement {

    private int quantity;





    private simplepdl_WorkDefinition simplepdl_workdefinition;




    private simplepdl_WorkDefinition simplepdl_workdefinition;




    private simplepdl_Ressource simplepdl_ressource;


    public simplepdl_RessourceSequence(
        int quantity    ) {
        super(
        );
        this.quantity = quantity;
    }


    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
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
    public simplepdl_Ressource getSimplepdl_ressource() {
        return simplepdl_ressource;
    }

    public void setSimplepdl_ressource(simplepdl_Ressource simplepdl_ressource) {
        this.simplepdl_ressource = simplepdl_ressource;
    }

}