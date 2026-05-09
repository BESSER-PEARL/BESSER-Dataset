





import java.util.List;
import java.util.ArrayList;

public class simplepdl_RessourceLink extends ProcessElement {

    private int weight;





    private simplepdl_RessourceSet simplepdl_ressourceset;


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

    public simplepdl_RessourceSet getSimplepdl_ressourceset() {
        return simplepdl_ressourceset;
    }

    public void setSimplepdl_ressourceset(simplepdl_RessourceSet simplepdl_ressourceset) {
        this.simplepdl_ressourceset = simplepdl_ressourceset;
    }

}