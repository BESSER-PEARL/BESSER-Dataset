





import java.util.List;
import java.util.ArrayList;

public class UML2_Classifier extends RedefinableElement, Type, Namespace {

    private boolean isAbstract;





    private UML2_InstanceSpecification uml2_instancespecification;


    public UML2_Classifier(
        boolean isAbstract    ) {
        super(
        );
        this.isAbstract = isAbstract;
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

}