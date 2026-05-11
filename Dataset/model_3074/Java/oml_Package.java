





import java.util.List;
import java.util.ArrayList;

public class oml_Package extends PackageableElement {






    private oml_PackageableElement oml_packageableelement;




    private List<oml_PackageableElement> oml_packageableelements;


    public oml_Package(
    ) {
        super(
        );
        this.oml_packageableelements = new ArrayList<>();
    }

    public oml_Package(
        ArrayList<oml_PackageableElement> oml_packageableelements    ) {
        this.oml_packageableelements = oml_packageableelements;
    }


    public oml_PackageableElement getOml_packageableelement() {
        return oml_packageableelement;
    }

    public void setOml_packageableelement(oml_PackageableElement oml_packageableelement) {
        this.oml_packageableelement = oml_packageableelement;
    }
    public List<oml_PackageableElement> getOml_packageableelements() {
        return oml_packageableelements;
    }

    public void addOml_packageableelement(Oml_packageableelement oml_packageableelement) {
        this.oml_packageableelements.add(oml_packageableelement);
    }

}