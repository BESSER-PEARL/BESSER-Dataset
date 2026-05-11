





import java.util.List;
import java.util.ArrayList;

public class umlMM_Package extends UMLModelElement {






    private umlMM_PackageElement umlmm_packageelement;




    private List<umlMM_PackageElement> umlmm_packageelements;


    public umlMM_Package(
    ) {
        super(
        );
        this.umlmm_packageelements = new ArrayList<>();
    }

    public umlMM_Package(
        ArrayList<umlMM_PackageElement> umlmm_packageelements    ) {
        this.umlmm_packageelements = umlmm_packageelements;
    }


    public umlMM_PackageElement getUmlmm_packageelement() {
        return umlmm_packageelement;
    }

    public void setUmlmm_packageelement(umlMM_PackageElement umlmm_packageelement) {
        this.umlmm_packageelement = umlmm_packageelement;
    }
    public List<umlMM_PackageElement> getUmlmm_packageelements() {
        return umlmm_packageelements;
    }

    public void addUmlmm_packageelement(Umlmm_packageelement umlmm_packageelement) {
        this.umlmm_packageelements.add(umlmm_packageelement);
    }

}