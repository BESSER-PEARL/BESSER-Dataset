





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_NamedElement extends Element {

    private String visibility;





    private UML2WithID_Namespace uml2withid_namespace;


    public UML2WithID_NamedElement(
        String visibility    ) {
        super(
        );
        this.visibility = visibility;
    }


    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }

    public UML2WithID_Namespace getUml2withid_namespace() {
        return uml2withid_namespace;
    }

    public void setUml2withid_namespace(UML2WithID_Namespace uml2withid_namespace) {
        this.uml2withid_namespace = uml2withid_namespace;
    }

}