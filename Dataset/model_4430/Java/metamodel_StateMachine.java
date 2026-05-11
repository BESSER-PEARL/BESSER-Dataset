





import java.util.List;
import java.util.ArrayList;

public class metamodel_StateMachine  {

    private String name;





    private metamodel_Behaviour metamodel_behaviour;


    public metamodel_StateMachine(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public metamodel_Behaviour getMetamodel_behaviour() {
        return metamodel_behaviour;
    }

    public void setMetamodel_behaviour(metamodel_Behaviour metamodel_behaviour) {
        this.metamodel_behaviour = metamodel_behaviour;
    }

}