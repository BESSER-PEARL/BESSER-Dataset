





import java.util.List;
import java.util.ArrayList;

public class PiServiceComposition_Policy  {

    private String name;





    private List<PiServiceComposition_BussinessCollaborator> piservicecomposition_bussinesscollaborators;




    private List<PiServiceComposition_Rule> piservicecomposition_rules;




    private PiServiceComposition_BussinessCollaborator piservicecomposition_bussinesscollaborator;




    private PiServiceComposition_ServiceActivity piservicecomposition_serviceactivity;




    private PiServiceComposition_Rule piservicecomposition_rule;




    private List<PiServiceComposition_Action> piservicecomposition_actions;




    private PiServiceComposition_CompositionServiceModel piservicecomposition_compositionservicemodel;




    private PiServiceComposition_Action piservicecomposition_action;


    public PiServiceComposition_Policy(
        String name    ) {
        this.name = name;
        this.piservicecomposition_bussinesscollaborators = new ArrayList<>();
        this.piservicecomposition_rules = new ArrayList<>();
        this.piservicecomposition_actions = new ArrayList<>();
    }

    public PiServiceComposition_Policy(
        String name        ArrayList<PiServiceComposition_BussinessCollaborator> piservicecomposition_bussinesscollaborators,        ArrayList<PiServiceComposition_Rule> piservicecomposition_rules,        ArrayList<PiServiceComposition_Action> piservicecomposition_actions    ) {
        this.name = name;
        this.piservicecomposition_bussinesscollaborators = piservicecomposition_bussinesscollaborators;
        this.piservicecomposition_rules = piservicecomposition_rules;
        this.piservicecomposition_actions = piservicecomposition_actions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<PiServiceComposition_BussinessCollaborator> getPiservicecomposition_bussinesscollaborators() {
        return piservicecomposition_bussinesscollaborators;
    }

    public void addPiservicecomposition_bussinesscollaborator(Piservicecomposition_bussinesscollaborator piservicecomposition_bussinesscollaborator) {
        this.piservicecomposition_bussinesscollaborators.add(piservicecomposition_bussinesscollaborator);
    }
    public List<PiServiceComposition_Rule> getPiservicecomposition_rules() {
        return piservicecomposition_rules;
    }

    public void addPiservicecomposition_rule(Piservicecomposition_rule piservicecomposition_rule) {
        this.piservicecomposition_rules.add(piservicecomposition_rule);
    }
    public PiServiceComposition_BussinessCollaborator getPiservicecomposition_bussinesscollaborator() {
        return piservicecomposition_bussinesscollaborator;
    }

    public void setPiservicecomposition_bussinesscollaborator(PiServiceComposition_BussinessCollaborator piservicecomposition_bussinesscollaborator) {
        this.piservicecomposition_bussinesscollaborator = piservicecomposition_bussinesscollaborator;
    }
    public PiServiceComposition_ServiceActivity getPiservicecomposition_serviceactivity() {
        return piservicecomposition_serviceactivity;
    }

    public void setPiservicecomposition_serviceactivity(PiServiceComposition_ServiceActivity piservicecomposition_serviceactivity) {
        this.piservicecomposition_serviceactivity = piservicecomposition_serviceactivity;
    }
    public PiServiceComposition_Rule getPiservicecomposition_rule() {
        return piservicecomposition_rule;
    }

    public void setPiservicecomposition_rule(PiServiceComposition_Rule piservicecomposition_rule) {
        this.piservicecomposition_rule = piservicecomposition_rule;
    }
    public List<PiServiceComposition_Action> getPiservicecomposition_actions() {
        return piservicecomposition_actions;
    }

    public void addPiservicecomposition_action(Piservicecomposition_action piservicecomposition_action) {
        this.piservicecomposition_actions.add(piservicecomposition_action);
    }
    public PiServiceComposition_CompositionServiceModel getPiservicecomposition_compositionservicemodel() {
        return piservicecomposition_compositionservicemodel;
    }

    public void setPiservicecomposition_compositionservicemodel(PiServiceComposition_CompositionServiceModel piservicecomposition_compositionservicemodel) {
        this.piservicecomposition_compositionservicemodel = piservicecomposition_compositionservicemodel;
    }
    public PiServiceComposition_Action getPiservicecomposition_action() {
        return piservicecomposition_action;
    }

    public void setPiservicecomposition_action(PiServiceComposition_Action piservicecomposition_action) {
        this.piservicecomposition_action = piservicecomposition_action;
    }

}