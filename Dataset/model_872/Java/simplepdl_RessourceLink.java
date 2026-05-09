





import java.util.List;
import java.util.ArrayList;

public class simplepdl_RessourceLink extends ProcessElement {

    private int weight;





    private simplepdl_WorkDefinition simplepdl_workdefinition;


    public simplepdl_RessourceLink(
        int weight    ) {
        super(
        );
        this.weight = weight;
    }


    public int getWeight() {
        return weight;
    }

    public void setWeight(int weight) {
        this.weight = weight;
    }

    public simplepdl_WorkDefinition getSimplepdl_workdefinition() {
        return simplepdl_workdefinition;
    }

    public void setSimplepdl_workdefinition(simplepdl_WorkDefinition simplepdl_workdefinition) {
        this.simplepdl_workdefinition = simplepdl_workdefinition;
    }

}