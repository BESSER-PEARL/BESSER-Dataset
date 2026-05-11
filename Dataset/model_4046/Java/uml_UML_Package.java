





import java.util.List;
import java.util.ArrayList;

public class uml_UML_Package extends UML_Namespace {






    private List<uml_UML_PackageableElement> uml_uml_packageableelements;


    public uml_UML_Package(
    ) {
        super(
        );
        this.uml_uml_packageableelements = new ArrayList<>();
    }

    public uml_UML_Package(
        ArrayList<uml_UML_PackageableElement> uml_uml_packageableelements    ) {
        this.uml_uml_packageableelements = uml_uml_packageableelements;
    }


    public List<uml_UML_PackageableElement> getUml_uml_packageableelements() {
        return uml_uml_packageableelements;
    }

    public void addUml_uml_packageableelement(Uml_uml_packageableelement uml_uml_packageableelement) {
        this.uml_uml_packageableelements.add(uml_uml_packageableelement);
    }

}