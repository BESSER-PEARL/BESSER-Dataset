





import java.util.List;
import java.util.ArrayList;

public class DOM_Javadoc extends Comment {






    private DOM_PackageDeclaration dom_packagedeclaration;




    private List<DOM_TagElement> dom_tagelements;




    private DOM_BodyDeclaration dom_bodydeclaration;


    public DOM_Javadoc(
    ) {
        super(
        );
        this.dom_tagelements = new ArrayList<>();
    }

    public DOM_Javadoc(
        ArrayList<DOM_TagElement> dom_tagelements    ) {
        this.dom_tagelements = dom_tagelements;
    }


    public DOM_PackageDeclaration getDom_packagedeclaration() {
        return dom_packagedeclaration;
    }

    public void setDom_packagedeclaration(DOM_PackageDeclaration dom_packagedeclaration) {
        this.dom_packagedeclaration = dom_packagedeclaration;
    }
    public List<DOM_TagElement> getDom_tagelements() {
        return dom_tagelements;
    }

    public void addDom_tagelement(Dom_tagelement dom_tagelement) {
        this.dom_tagelements.add(dom_tagelement);
    }
    public DOM_BodyDeclaration getDom_bodydeclaration() {
        return dom_bodydeclaration;
    }

    public void setDom_bodydeclaration(DOM_BodyDeclaration dom_bodydeclaration) {
        this.dom_bodydeclaration = dom_bodydeclaration;
    }

}