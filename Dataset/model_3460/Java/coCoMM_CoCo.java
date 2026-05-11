





import java.util.List;
import java.util.ArrayList;

public class coCoMM_CoCo  {






    private List<coCoMM_Project> cocomm_projects;




    private List<coCoMM_AttributeType> cocomm_attributetypes;




    private List<coCoMM_DecisionRule> cocomm_decisionrules;




    private List<coCoMM_Stakeholder> cocomm_stakeholders;




    private List<coCoMM_FeatureModel> cocomm_featuremodels;


    public coCoMM_CoCo(
    ) {
        this.cocomm_projects = new ArrayList<>();
        this.cocomm_attributetypes = new ArrayList<>();
        this.cocomm_decisionrules = new ArrayList<>();
        this.cocomm_stakeholders = new ArrayList<>();
        this.cocomm_featuremodels = new ArrayList<>();
    }

    public coCoMM_CoCo(
        ArrayList<coCoMM_Project> cocomm_projects,        ArrayList<coCoMM_AttributeType> cocomm_attributetypes,        ArrayList<coCoMM_DecisionRule> cocomm_decisionrules,        ArrayList<coCoMM_Stakeholder> cocomm_stakeholders,        ArrayList<coCoMM_FeatureModel> cocomm_featuremodels    ) {
        this.cocomm_projects = cocomm_projects;
        this.cocomm_attributetypes = cocomm_attributetypes;
        this.cocomm_decisionrules = cocomm_decisionrules;
        this.cocomm_stakeholders = cocomm_stakeholders;
        this.cocomm_featuremodels = cocomm_featuremodels;
    }


    public List<coCoMM_Project> getCocomm_projects() {
        return cocomm_projects;
    }

    public void addCocomm_project(Cocomm_project cocomm_project) {
        this.cocomm_projects.add(cocomm_project);
    }
    public List<coCoMM_AttributeType> getCocomm_attributetypes() {
        return cocomm_attributetypes;
    }

    public void addCocomm_attributetype(Cocomm_attributetype cocomm_attributetype) {
        this.cocomm_attributetypes.add(cocomm_attributetype);
    }
    public List<coCoMM_DecisionRule> getCocomm_decisionrules() {
        return cocomm_decisionrules;
    }

    public void addCocomm_decisionrule(Cocomm_decisionrule cocomm_decisionrule) {
        this.cocomm_decisionrules.add(cocomm_decisionrule);
    }
    public List<coCoMM_Stakeholder> getCocomm_stakeholders() {
        return cocomm_stakeholders;
    }

    public void addCocomm_stakeholder(Cocomm_stakeholder cocomm_stakeholder) {
        this.cocomm_stakeholders.add(cocomm_stakeholder);
    }
    public List<coCoMM_FeatureModel> getCocomm_featuremodels() {
        return cocomm_featuremodels;
    }

    public void addCocomm_featuremodel(Cocomm_featuremodel cocomm_featuremodel) {
        this.cocomm_featuremodels.add(cocomm_featuremodel);
    }

}