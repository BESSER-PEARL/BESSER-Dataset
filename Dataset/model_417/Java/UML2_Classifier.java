





import java.util.List;
import java.util.ArrayList;

public class UML2_Classifier extends Type, RedefinableElement, Namespace {

    private boolean isAbstract;





    private UML2_CreateObjectAction uml2_createobjectaction;




    private List<UML2_NamedElement> uml2_namedelements;




    private UML2_Class uml2_class;




    private UML2_InstanceSpecification uml2_instancespecification;


    public UML2_Classifier(
        boolean isAbstract    ) {
        super(
        );
        this.isAbstract = isAbstract;
        this.uml2_namedelements = new ArrayList<>();
    }

    public UML2_Classifier(
        boolean isAbstract        ArrayList<UML2_NamedElement> uml2_namedelements    ) {
        this.isAbstract = isAbstract;
        this.uml2_namedelements = uml2_namedelements;
    }

    public boolean getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(boolean isAbstract) {
        this.isAbstract = isAbstract;
    }

    public UML2_CreateObjectAction getUml2_createobjectaction() {
        return uml2_createobjectaction;
    }

    public void setUml2_createobjectaction(UML2_CreateObjectAction uml2_createobjectaction) {
        this.uml2_createobjectaction = uml2_createobjectaction;
    }
    public List<UML2_NamedElement> getUml2_namedelements() {
        return uml2_namedelements;
    }

    public void addUml2_namedelement(Uml2_namedelement uml2_namedelement) {
        this.uml2_namedelements.add(uml2_namedelement);
    }
    public UML2_Class getUml2_class() {
        return uml2_class;
    }

    public void setUml2_class(UML2_Class uml2_class) {
        this.uml2_class = uml2_class;
    }
    public UML2_InstanceSpecification getUml2_instancespecification() {
        return uml2_instancespecification;
    }

    public void setUml2_instancespecification(UML2_InstanceSpecification uml2_instancespecification) {
        this.uml2_instancespecification = uml2_instancespecification;
    }

}