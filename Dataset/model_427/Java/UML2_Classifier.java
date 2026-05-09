





import java.util.List;
import java.util.ArrayList;

public class UML2_Classifier extends Namespace, Type, RedefinableElement {

    private boolean isAbstract;





    private UML2_CreateObjectAction uml2_createobjectaction;


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

    public UML2_CreateObjectAction getUml2_createobjectaction() {
        return uml2_createobjectaction;
    }

    public void setUml2_createobjectaction(UML2_CreateObjectAction uml2_createobjectaction) {
        this.uml2_createobjectaction = uml2_createobjectaction;
    }

}