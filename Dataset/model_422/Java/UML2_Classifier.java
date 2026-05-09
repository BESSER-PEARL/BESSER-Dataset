





import java.util.List;
import java.util.ArrayList;

public class UML2_Classifier extends Type, RedefinableElement, Namespace {

    private boolean isAbstract;





    private UML2_InstanceSpecification uml2_instancespecification;




    private List<UML2_Generalization> uml2_generalizations;




    private UML2_CreateObjectAction uml2_createobjectaction;




    private UML2_Generalization uml2_generalization;


    public UML2_Classifier(
        boolean isAbstract    ) {
        super(
        );
        this.isAbstract = isAbstract;
        this.uml2_generalizations = new ArrayList<>();
    }

    public UML2_Classifier(
        boolean isAbstract        ArrayList<UML2_Generalization> uml2_generalizations    ) {
        this.isAbstract = isAbstract;
        this.uml2_generalizations = uml2_generalizations;
    }

    public boolean getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(boolean isAbstract) {
        this.isAbstract = isAbstract;
    }

    public UML2_InstanceSpecification getUml2_instancespecification() {
        return uml2_instancespecification;
    }

    public void setUml2_instancespecification(UML2_InstanceSpecification uml2_instancespecification) {
        this.uml2_instancespecification = uml2_instancespecification;
    }
    public List<UML2_Generalization> getUml2_generalizations() {
        return uml2_generalizations;
    }

    public void addUml2_generalization(Uml2_generalization uml2_generalization) {
        this.uml2_generalizations.add(uml2_generalization);
    }
    public UML2_CreateObjectAction getUml2_createobjectaction() {
        return uml2_createobjectaction;
    }

    public void setUml2_createobjectaction(UML2_CreateObjectAction uml2_createobjectaction) {
        this.uml2_createobjectaction = uml2_createobjectaction;
    }
    public UML2_Generalization getUml2_generalization() {
        return uml2_generalization;
    }

    public void setUml2_generalization(UML2_Generalization uml2_generalization) {
        this.uml2_generalization = uml2_generalization;
    }

}