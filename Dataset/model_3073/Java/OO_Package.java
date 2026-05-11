





import java.util.List;
import java.util.ArrayList;

public class OO_Package extends PackageableElement {






    private List<OO_PackageableElement> oo_packageableelements;




    private OO_PackageableElement oo_packageableelement;


    public OO_Package(
    ) {
        super(
        );
        this.oo_packageableelements = new ArrayList<>();
    }

    public OO_Package(
        ArrayList<OO_PackageableElement> oo_packageableelements    ) {
        this.oo_packageableelements = oo_packageableelements;
    }


    public List<OO_PackageableElement> getOo_packageableelements() {
        return oo_packageableelements;
    }

    public void addOo_packageableelement(Oo_packageableelement oo_packageableelement) {
        this.oo_packageableelements.add(oo_packageableelement);
    }
    public OO_PackageableElement getOo_packageableelement() {
        return oo_packageableelement;
    }

    public void setOo_packageableelement(OO_PackageableElement oo_packageableelement) {
        this.oo_packageableelement = oo_packageableelement;
    }

}