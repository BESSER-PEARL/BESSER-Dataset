





import java.util.List;
import java.util.ArrayList;

public class MetaModel_EvolutionStyle  {

    private String name;





    private MetaModel_FinalState metamodel_finalstate;




    private List<MetaModel_IntermidiateState> metamodel_intermidiatestates;


    public MetaModel_EvolutionStyle(
        String name    ) {
        this.name = name;
        this.metamodel_intermidiatestates = new ArrayList<>();
    }

    public MetaModel_EvolutionStyle(
        String name        ArrayList<MetaModel_IntermidiateState> metamodel_intermidiatestates    ) {
        this.name = name;
        this.metamodel_intermidiatestates = metamodel_intermidiatestates;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public MetaModel_FinalState getMetamodel_finalstate() {
        return metamodel_finalstate;
    }

    public void setMetamodel_finalstate(MetaModel_FinalState metamodel_finalstate) {
        this.metamodel_finalstate = metamodel_finalstate;
    }
    public List<MetaModel_IntermidiateState> getMetamodel_intermidiatestates() {
        return metamodel_intermidiatestates;
    }

    public void addMetamodel_intermidiatestate(Metamodel_intermidiatestate metamodel_intermidiatestate) {
        this.metamodel_intermidiatestates.add(metamodel_intermidiatestate);
    }

}