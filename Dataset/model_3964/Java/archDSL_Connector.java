





import java.util.List;
import java.util.ArrayList;

public class archDSL_Connector  {

    private String name;





    private List<archDSL_Behavior> archdsl_behaviors;




    private archDSL_Model archdsl_model;


    public archDSL_Connector(
        String name    ) {
        this.name = name;
        this.archdsl_behaviors = new ArrayList<>();
    }

    public archDSL_Connector(
        String name        ArrayList<archDSL_Behavior> archdsl_behaviors    ) {
        this.name = name;
        this.archdsl_behaviors = archdsl_behaviors;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<archDSL_Behavior> getArchdsl_behaviors() {
        return archdsl_behaviors;
    }

    public void addArchdsl_behavior(Archdsl_behavior archdsl_behavior) {
        this.archdsl_behaviors.add(archdsl_behavior);
    }
    public archDSL_Model getArchdsl_model() {
        return archdsl_model;
    }

    public void setArchdsl_model(archDSL_Model archdsl_model) {
        this.archdsl_model = archdsl_model;
    }

}