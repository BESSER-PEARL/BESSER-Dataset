





import java.util.List;
import java.util.ArrayList;

public class ConceptASE_SwitchPosition extends Thing {

    private String SwitchPosition_switchState;





    private ConceptASE_Route conceptase_route;




    private List<ConceptASE_Route> conceptase_routes;




    private List<ConceptASE_Switch> conceptase_switchs;




    private ConceptASE_Switch conceptase_switch;


    public ConceptASE_SwitchPosition(
        String SwitchPosition_switchState    ) {
        super(
        );
        this.SwitchPosition_switchState = SwitchPosition_switchState;
        this.conceptase_routes = new ArrayList<>();
        this.conceptase_switchs = new ArrayList<>();
    }

    public ConceptASE_SwitchPosition(
        String SwitchPosition_switchState        ArrayList<ConceptASE_Route> conceptase_routes,        ArrayList<ConceptASE_Switch> conceptase_switchs    ) {
        this.SwitchPosition_switchState = SwitchPosition_switchState;
        this.conceptase_routes = conceptase_routes;
        this.conceptase_switchs = conceptase_switchs;
    }

    public String getSwitchposition_switchstate() {
        return SwitchPosition_switchState;
    }

    public void setSwitchposition_switchstate(String SwitchPosition_switchState) {
        this.SwitchPosition_switchState = SwitchPosition_switchState;
    }

    public ConceptASE_Route getConceptase_route() {
        return conceptase_route;
    }

    public void setConceptase_route(ConceptASE_Route conceptase_route) {
        this.conceptase_route = conceptase_route;
    }
    public List<ConceptASE_Route> getConceptase_routes() {
        return conceptase_routes;
    }

    public void addConceptase_route(Conceptase_route conceptase_route) {
        this.conceptase_routes.add(conceptase_route);
    }
    public List<ConceptASE_Switch> getConceptase_switchs() {
        return conceptase_switchs;
    }

    public void addConceptase_switch(Conceptase_switch conceptase_switch) {
        this.conceptase_switchs.add(conceptase_switch);
    }
    public ConceptASE_Switch getConceptase_switch() {
        return conceptase_switch;
    }

    public void setConceptase_switch(ConceptASE_Switch conceptase_switch) {
        this.conceptase_switch = conceptase_switch;
    }

}