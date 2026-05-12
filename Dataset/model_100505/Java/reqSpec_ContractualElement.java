





import java.util.List;
import java.util.ArrayList;

public class reqSpec_ContractualElement  {

    private boolean dropped;
    private String dropRationale;
    private String targetDescription;
    private String issues;
    private String name;
    private String title;





    private reqSpec_Rationale reqspec_rationale;




    private List<reqSpec_AVariableDeclaration> reqspec_avariabledeclarations;




    private reqSpec_ComponentClassifier reqspec_componentclassifier;




    private reqSpec_WhenCondition reqspec_whencondition;




    private reqSpec_NamedElement reqspec_namedelement;




    private reqSpec_Description reqspec_description;




    private List<reqSpec_Category> reqspec_categorys;


    public reqSpec_ContractualElement(
        boolean dropped,        String dropRationale,        String targetDescription,        String issues,        String name,        String title    ) {
        this.dropped = dropped;
        this.dropRationale = dropRationale;
        this.targetDescription = targetDescription;
        this.issues = issues;
        this.name = name;
        this.title = title;
        this.reqspec_avariabledeclarations = new ArrayList<>();
        this.reqspec_categorys = new ArrayList<>();
    }

    public reqSpec_ContractualElement(
        boolean dropped,        String dropRationale,        String targetDescription,        String issues,        String name,        String title        ArrayList<reqSpec_AVariableDeclaration> reqspec_avariabledeclarations,        ArrayList<reqSpec_Category> reqspec_categorys    ) {
        this.dropped = dropped;
        this.dropRationale = dropRationale;
        this.targetDescription = targetDescription;
        this.issues = issues;
        this.name = name;
        this.title = title;
        this.reqspec_avariabledeclarations = reqspec_avariabledeclarations;
        this.reqspec_categorys = reqspec_categorys;
    }

    public boolean getDropped() {
        return dropped;
    }

    public void setDropped(boolean dropped) {
        this.dropped = dropped;
    }
    public String getDroprationale() {
        return dropRationale;
    }

    public void setDroprationale(String dropRationale) {
        this.dropRationale = dropRationale;
    }
    public String getTargetdescription() {
        return targetDescription;
    }

    public void setTargetdescription(String targetDescription) {
        this.targetDescription = targetDescription;
    }
    public String getIssues() {
        return issues;
    }

    public void setIssues(String issues) {
        this.issues = issues;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public reqSpec_Rationale getReqspec_rationale() {
        return reqspec_rationale;
    }

    public void setReqspec_rationale(reqSpec_Rationale reqspec_rationale) {
        this.reqspec_rationale = reqspec_rationale;
    }
    public List<reqSpec_AVariableDeclaration> getReqspec_avariabledeclarations() {
        return reqspec_avariabledeclarations;
    }

    public void addReqspec_avariabledeclaration(Reqspec_avariabledeclaration reqspec_avariabledeclaration) {
        this.reqspec_avariabledeclarations.add(reqspec_avariabledeclaration);
    }
    public reqSpec_ComponentClassifier getReqspec_componentclassifier() {
        return reqspec_componentclassifier;
    }

    public void setReqspec_componentclassifier(reqSpec_ComponentClassifier reqspec_componentclassifier) {
        this.reqspec_componentclassifier = reqspec_componentclassifier;
    }
    public reqSpec_WhenCondition getReqspec_whencondition() {
        return reqspec_whencondition;
    }

    public void setReqspec_whencondition(reqSpec_WhenCondition reqspec_whencondition) {
        this.reqspec_whencondition = reqspec_whencondition;
    }
    public reqSpec_NamedElement getReqspec_namedelement() {
        return reqspec_namedelement;
    }

    public void setReqspec_namedelement(reqSpec_NamedElement reqspec_namedelement) {
        this.reqspec_namedelement = reqspec_namedelement;
    }
    public reqSpec_Description getReqspec_description() {
        return reqspec_description;
    }

    public void setReqspec_description(reqSpec_Description reqspec_description) {
        this.reqspec_description = reqspec_description;
    }
    public List<reqSpec_Category> getReqspec_categorys() {
        return reqspec_categorys;
    }

    public void addReqspec_category(Reqspec_category reqspec_category) {
        this.reqspec_categorys.add(reqspec_category);
    }

}