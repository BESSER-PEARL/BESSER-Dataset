





import java.util.List;
import java.util.ArrayList;

public class SimpleUML_UmlPackage extends UmlModelElement {






    private List<SimpleUML_UmlPackageElement> simpleuml_umlpackageelements;




    private SimpleUML_UmlPackageElement simpleuml_umlpackageelement;


    public SimpleUML_UmlPackage(
    ) {
        super(
        );
        this.simpleuml_umlpackageelements = new ArrayList<>();
    }

    public SimpleUML_UmlPackage(
        ArrayList<SimpleUML_UmlPackageElement> simpleuml_umlpackageelements    ) {
        this.simpleuml_umlpackageelements = simpleuml_umlpackageelements;
    }


    public List<SimpleUML_UmlPackageElement> getSimpleuml_umlpackageelements() {
        return simpleuml_umlpackageelements;
    }

    public void addSimpleuml_umlpackageelement(Simpleuml_umlpackageelement simpleuml_umlpackageelement) {
        this.simpleuml_umlpackageelements.add(simpleuml_umlpackageelement);
    }
    public SimpleUML_UmlPackageElement getSimpleuml_umlpackageelement() {
        return simpleuml_umlpackageelement;
    }

    public void setSimpleuml_umlpackageelement(SimpleUML_UmlPackageElement simpleuml_umlpackageelement) {
        this.simpleuml_umlpackageelement = simpleuml_umlpackageelement;
    }

}