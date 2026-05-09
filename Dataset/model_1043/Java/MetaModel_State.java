





import java.util.List;
import java.util.ArrayList;

public class MetaModel_State  {

    private String name;





    private MetaModel_Transition metamodel_transition;




    private MetaModel_IntermidiateState metamodel_intermidiatestate;




    private MetaModel_FinalState metamodel_finalstate;




    private MetaModel_IntermidiateState metamodel_intermidiatestate;




    private MetaModel_InitialState metamodel_initialstate;




    private MetaModel_Transition metamodel_transition;


    public MetaModel_State(
        String name    ) {
        this.name = name;
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
    public MetaModel_IntermidiateState getMetamodel_intermidiatestate() {
        return metamodel_intermidiatestate;
    }

    public void setMetamodel_intermidiatestate(MetaModel_IntermidiateState metamodel_intermidiatestate) {
        this.metamodel_intermidiatestate = metamodel_intermidiatestate;
    }
    public MetaModel_FinalState getMetamodel_finalstate() {
        return metamodel_finalstate;
    }

    public void setMetamodel_finalstate(MetaModel_FinalState metamodel_finalstate) {
        this.metamodel_finalstate = metamodel_finalstate;
    }
    public MetaModel_IntermidiateState getMetamodel_intermidiatestate() {
        return metamodel_intermidiatestate;
    }

    public void setMetamodel_intermidiatestate(MetaModel_IntermidiateState metamodel_intermidiatestate) {
        this.metamodel_intermidiatestate = metamodel_intermidiatestate;
    }
    public MetaModel_InitialState getMetamodel_initialstate() {
        return metamodel_initialstate;
    }

    public void setMetamodel_initialstate(MetaModel_InitialState metamodel_initialstate) {
        this.metamodel_initialstate = metamodel_initialstate;
    }
    public MetaModel_Transition getMetamodel_transition() {
        return metamodel_transition;
    }

    public void setMetamodel_transition(MetaModel_Transition metamodel_transition) {
        this.metamodel_transition = metamodel_transition;
    }

}