





import java.util.List;
import java.util.ArrayList;

public class UMLMM_Package extends TemplateableElement, Namespace, PackageableElement {






    private List<UMLMM_PackageableElement> umlmm_packageableelements;


    public UMLMM_Package(
    ) {
        super(
        );
        this.umlmm_packageableelements = new ArrayList<>();
    }

    public UMLMM_Package(
        ArrayList<UMLMM_PackageableElement> umlmm_packageableelements    ) {
        this.umlmm_packageableelements = umlmm_packageableelements;
    }


    public List<UMLMM_PackageableElement> getUmlmm_packageableelements() {
        return umlmm_packageableelements;
    }

    public void addUmlmm_packageableelement(Umlmm_packageableelement umlmm_packageableelement) {
        this.umlmm_packageableelements.add(umlmm_packageableelement);
    }

}