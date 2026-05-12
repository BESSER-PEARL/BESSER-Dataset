





import java.util.List;
import java.util.ArrayList;

public class reqSpec_Requirement extends ContractualElement {

    private boolean connections;
    private String componentCategory;
    private String exceptionText;





    private List<reqSpec_Requirement> reqspec_requirements;




    private List<reqSpec_AVariableDeclaration> reqspec_avariabledeclarations;




    private reqSpec_RequirementSet reqspec_requirementset;




    private reqSpec_Requirement reqspec_requirement;




    private reqSpec_EObject reqspec_eobject;




    private reqSpec_ContractualElement reqspec_contractualelement;




    private reqSpec_Requirement reqspec_requirement;




    private reqSpec_Requirement reqspec_requirement;


    public reqSpec_Requirement(
        boolean connections,        String componentCategory,        String exceptionText    ) {
        super(
        );
        this.connections = connections;
        this.componentCategory = componentCategory;
        this.exceptionText = exceptionText;
        this.reqspec_requirements = new ArrayList<>();
        this.reqspec_avariabledeclarations = new ArrayList<>();
    }

    public reqSpec_Requirement(
        boolean connections,        String componentCategory,        String exceptionText        ArrayList<reqSpec_Requirement> reqspec_requirements,        ArrayList<reqSpec_AVariableDeclaration> reqspec_avariabledeclarations    ) {
        this.connections = connections;
        this.componentCategory = componentCategory;
        this.exceptionText = exceptionText;
        this.reqspec_requirements = reqspec_requirements;
        this.reqspec_avariabledeclarations = reqspec_avariabledeclarations;
    }

    public boolean getConnections() {
        return connections;
    }

    public void setConnections(boolean connections) {
        this.connections = connections;
    }
    public String getComponentcategory() {
        return componentCategory;
    }

    public void setComponentcategory(String componentCategory) {
        this.componentCategory = componentCategory;
    }
    public String getExceptiontext() {
        return exceptionText;
    }

    public void setExceptiontext(String exceptionText) {
        this.exceptionText = exceptionText;
    }

    public List<reqSpec_Requirement> getReqspec_requirements() {
        return reqspec_requirements;
    }

    public void addReqspec_requirement(Reqspec_requirement reqspec_requirement) {
        this.reqspec_requirements.add(reqspec_requirement);
    }
    public List<reqSpec_AVariableDeclaration> getReqspec_avariabledeclarations() {
        return reqspec_avariabledeclarations;
    }

    public void addReqspec_avariabledeclaration(Reqspec_avariabledeclaration reqspec_avariabledeclaration) {
        this.reqspec_avariabledeclarations.add(reqspec_avariabledeclaration);
    }
    public reqSpec_RequirementSet getReqspec_requirementset() {
        return reqspec_requirementset;
    }

    public void setReqspec_requirementset(reqSpec_RequirementSet reqspec_requirementset) {
        this.reqspec_requirementset = reqspec_requirementset;
    }
    public reqSpec_Requirement getReqspec_requirement() {
        return reqspec_requirement;
    }

    public void setReqspec_requirement(reqSpec_Requirement reqspec_requirement) {
        this.reqspec_requirement = reqspec_requirement;
    }
    public reqSpec_EObject getReqspec_eobject() {
        return reqspec_eobject;
    }

    public void setReqspec_eobject(reqSpec_EObject reqspec_eobject) {
        this.reqspec_eobject = reqspec_eobject;
    }
    public reqSpec_ContractualElement getReqspec_contractualelement() {
        return reqspec_contractualelement;
    }

    public void setReqspec_contractualelement(reqSpec_ContractualElement reqspec_contractualelement) {
        this.reqspec_contractualelement = reqspec_contractualelement;
    }
    public reqSpec_Requirement getReqspec_requirement() {
        return reqspec_requirement;
    }

    public void setReqspec_requirement(reqSpec_Requirement reqspec_requirement) {
        this.reqspec_requirement = reqspec_requirement;
    }
    public reqSpec_Requirement getReqspec_requirement() {
        return reqspec_requirement;
    }

    public void setReqspec_requirement(reqSpec_Requirement reqspec_requirement) {
        this.reqspec_requirement = reqspec_requirement;
    }

}