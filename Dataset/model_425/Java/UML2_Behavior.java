





import java.util.List;
import java.util.ArrayList;

public class UML2_Behavior extends Class {






    private UML2_BehavioralFeature uml2_behavioralfeature;




    private UML2_OpaqueExpression uml2_opaqueexpression;




    private UML2_BehavioredClassifier uml2_behavioredclassifier;




    private UML2_BehavioredClassifier uml2_behavioredclassifier;




    private List<UML2_ParameterSet> uml2_parametersets;


    public UML2_Behavior(
    ) {
        super(
        );
        this.uml2_parametersets = new ArrayList<>();
    }

    public UML2_Behavior(
        ArrayList<UML2_ParameterSet> uml2_parametersets    ) {
        this.uml2_parametersets = uml2_parametersets;
    }


    public UML2_BehavioralFeature getUml2_behavioralfeature() {
        return uml2_behavioralfeature;
    }

    public void setUml2_behavioralfeature(UML2_BehavioralFeature uml2_behavioralfeature) {
        this.uml2_behavioralfeature = uml2_behavioralfeature;
    }
    public UML2_OpaqueExpression getUml2_opaqueexpression() {
        return uml2_opaqueexpression;
    }

    public void setUml2_opaqueexpression(UML2_OpaqueExpression uml2_opaqueexpression) {
        this.uml2_opaqueexpression = uml2_opaqueexpression;
    }
    public UML2_BehavioredClassifier getUml2_behavioredclassifier() {
        return uml2_behavioredclassifier;
    }

    public void setUml2_behavioredclassifier(UML2_BehavioredClassifier uml2_behavioredclassifier) {
        this.uml2_behavioredclassifier = uml2_behavioredclassifier;
    }
    public UML2_BehavioredClassifier getUml2_behavioredclassifier() {
        return uml2_behavioredclassifier;
    }

    public void setUml2_behavioredclassifier(UML2_BehavioredClassifier uml2_behavioredclassifier) {
        this.uml2_behavioredclassifier = uml2_behavioredclassifier;
    }
    public List<UML2_ParameterSet> getUml2_parametersets() {
        return uml2_parametersets;
    }

    public void addUml2_parameterset(Uml2_parameterset uml2_parameterset) {
        this.uml2_parametersets.add(uml2_parameterset);
    }

}