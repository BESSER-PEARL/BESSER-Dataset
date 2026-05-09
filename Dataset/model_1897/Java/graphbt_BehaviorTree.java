





import java.util.List;
import java.util.ArrayList;

public class graphbt_BehaviorTree  {

    private String name;





    private graphbt_BEModel graphbt_bemodel;


    public graphbt_BehaviorTree(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public graphbt_BEModel getGraphbt_bemodel() {
        return graphbt_bemodel;
    }

    public void setGraphbt_bemodel(graphbt_BEModel graphbt_bemodel) {
        this.graphbt_bemodel = graphbt_bemodel;
    }

}