





import java.util.List;
import java.util.ArrayList;

public class uml_Package extends PackageableElement, Namespace, TemplateableElement {






    private List<uml_PackageableElement> uml_packageableelements;


    public uml_Package(
    ) {
        super(
        );
        this.uml_packageableelements = new ArrayList<>();
    }

    public uml_Package(
        ArrayList<uml_PackageableElement> uml_packageableelements    ) {
        this.uml_packageableelements = uml_packageableelements;
    }


    public List<uml_PackageableElement> getUml_packageableelements() {
        return uml_packageableelements;
    }

    public void addUml_packageableelement(Uml_packageableelement uml_packageableelement) {
        this.uml_packageableelements.add(uml_packageableelement);
    }

}