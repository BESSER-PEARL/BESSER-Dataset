





import java.util.List;
import java.util.ArrayList;

public class UML2_ElementImport extends DirectedRelationship {

    private String visibility;





    private UML2_PackageableElement uml2_packageableelement;


    public UML2_ElementImport(
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

    public UML2_PackageableElement getUml2_packageableelement() {
        return uml2_packageableelement;
    }

    public void setUml2_packageableelement(UML2_PackageableElement uml2_packageableelement) {
        this.uml2_packageableelement = uml2_packageableelement;
    }

}