





import java.util.List;
import java.util.ArrayList;

public class MetaModel_Operation  {

    private String time;
    private String cost;
    private String name;





    private MetaModel_Transition metamodel_transition;


    public MetaModel_Operation(
        String time,        String cost,        String name    ) {
        this.time = time;
        this.cost = cost;
        this.name = name;
    }


    public String getTime() {
        return time;
    }

    public void setTime(String time) {
        this.time = time;
    }
    public String getCost() {
        return cost;
    }

    public void setCost(String cost) {
        this.cost = cost;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public MetaModel_Transition getMetamodel_transition() {
        return metamodel_transition;
    }

    public void setMetamodel_transition(MetaModel_Transition metamodel_transition) {
        this.metamodel_transition = metamodel_transition;
    }

}