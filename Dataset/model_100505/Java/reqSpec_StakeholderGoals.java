





import java.util.List;
import java.util.ArrayList;

public class reqSpec_StakeholderGoals extends ReqRoot {

    private String componentCategory;





    private List<reqSpec_GlobalConstants> reqspec_globalconstantss;




    private List<reqSpec_Goal> reqspec_goals;




    private reqSpec_ComponentClassifier reqspec_componentclassifier;




    private List<reqSpec_AVariableDeclaration> reqspec_avariabledeclarations;


    public reqSpec_StakeholderGoals(
        String componentCategory    ) {
        super(
        );
        this.componentCategory = componentCategory;
        this.reqspec_globalconstantss = new ArrayList<>();
        this.reqspec_goals = new ArrayList<>();
        this.reqspec_avariabledeclarations = new ArrayList<>();
    }

    public reqSpec_StakeholderGoals(
        String componentCategory        ArrayList<reqSpec_GlobalConstants> reqspec_globalconstantss,        ArrayList<reqSpec_Goal> reqspec_goals,        ArrayList<reqSpec_AVariableDeclaration> reqspec_avariabledeclarations    ) {
        this.componentCategory = componentCategory;
        this.reqspec_globalconstantss = reqspec_globalconstantss;
        this.reqspec_goals = reqspec_goals;
        this.reqspec_avariabledeclarations = reqspec_avariabledeclarations;
    }

    public String getComponentcategory() {
        return componentCategory;
    }

    public void setComponentcategory(String componentCategory) {
        this.componentCategory = componentCategory;
    }

    public List<reqSpec_GlobalConstants> getReqspec_globalconstantss() {
        return reqspec_globalconstantss;
    }

    public void addReqspec_globalconstants(Reqspec_globalconstants reqspec_globalconstants) {
        this.reqspec_globalconstantss.add(reqspec_globalconstants);
    }
    public List<reqSpec_Goal> getReqspec_goals() {
        return reqspec_goals;
    }

    public void addReqspec_goal(Reqspec_goal reqspec_goal) {
        this.reqspec_goals.add(reqspec_goal);
    }
    public reqSpec_ComponentClassifier getReqspec_componentclassifier() {
        return reqspec_componentclassifier;
    }

    public void setReqspec_componentclassifier(reqSpec_ComponentClassifier reqspec_componentclassifier) {
        this.reqspec_componentclassifier = reqspec_componentclassifier;
    }
    public List<reqSpec_AVariableDeclaration> getReqspec_avariabledeclarations() {
        return reqspec_avariabledeclarations;
    }

    public void addReqspec_avariabledeclaration(Reqspec_avariabledeclaration reqspec_avariabledeclaration) {
        this.reqspec_avariabledeclarations.add(reqspec_avariabledeclaration);
    }

}