





import java.util.List;
import java.util.ArrayList;

public class simplepdl_RessourceLink extends ProcessElement {

    private int weight;





    private simplepdl_Ressource simplepdl_ressource;


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

    public simplepdl_Ressource getSimplepdl_ressource() {
        return simplepdl_ressource;
    }

    public void setSimplepdl_ressource(simplepdl_Ressource simplepdl_ressource) {
        this.simplepdl_ressource = simplepdl_ressource;
    }

}