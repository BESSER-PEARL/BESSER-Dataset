





import java.util.List;
import java.util.ArrayList;

public class UML2_NamedElement  {

    private String visibility;





    private UML2_Namespace uml2_namespace;


    public UML2_NamedElement(
        String visibility    ) {
        this.visibility = visibility;
    }


    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }

    public UML2_Namespace getUml2_namespace() {
        return uml2_namespace;
    }

    public void setUml2_namespace(UML2_Namespace uml2_namespace) {
        this.uml2_namespace = uml2_namespace;
    }

}