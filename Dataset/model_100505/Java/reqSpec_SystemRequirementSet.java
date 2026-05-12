





import java.util.List;
import java.util.ArrayList;

public class reqSpec_SystemRequirementSet extends RequirementSet {






    private List<reqSpec_IncludeGlobalRequirement> reqspec_includeglobalrequirements;




    private reqSpec_ComponentClassifier reqspec_componentclassifier;


    public reqSpec_SystemRequirementSet(
    ) {
        super(
        );
        this.reqspec_includeglobalrequirements = new ArrayList<>();
    }

    public reqSpec_SystemRequirementSet(
        ArrayList<reqSpec_IncludeGlobalRequirement> reqspec_includeglobalrequirements    ) {
        this.reqspec_includeglobalrequirements = reqspec_includeglobalrequirements;
    }


    public List<reqSpec_IncludeGlobalRequirement> getReqspec_includeglobalrequirements() {
        return reqspec_includeglobalrequirements;
    }

    public void addReqspec_includeglobalrequirement(Reqspec_includeglobalrequirement reqspec_includeglobalrequirement) {
        this.reqspec_includeglobalrequirements.add(reqspec_includeglobalrequirement);
    }
    public reqSpec_ComponentClassifier getReqspec_componentclassifier() {
        return reqspec_componentclassifier;
    }

    public void setReqspec_componentclassifier(reqSpec_ComponentClassifier reqspec_componentclassifier) {
        this.reqspec_componentclassifier = reqspec_componentclassifier;
    }

}